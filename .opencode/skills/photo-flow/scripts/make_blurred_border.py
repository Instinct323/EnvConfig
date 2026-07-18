from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np

to_2tuple = lambda x: x if x is None or isinstance(x, (list, tuple)) else (x,) * 2


def make_blurred_border(src: np.ndarray,
                        img_size: int | tuple[int, int] = None,
                        aspect_ratio: float = None):
    int_round = lambda x: np.round(x).astype(np.int64)
    src_size = np.array(src.shape[1::-1])
    img_size = np.array(to_2tuple(img_size))
    if not img_size and aspect_ratio:
        s1 = src_size[1] / np.array((aspect_ratio, 1))
        s2 = src_size[0] * np.array((1, aspect_ratio))
        img_size = int_round(max((s1, s2), key=np.prod))
    assert np.all(img_size), "No target size specified."
    rs = np.sort(img_size / src_size)
    fg_size = int_round(rs[0] * src_size)
    fg = cv2.resize(src, fg_size)
    bg_size = int_round(rs[1] * src_size)
    bg = cv2.resize(src, bg_size)
    pad_size = img_size - fg_size
    if np.any(pad_size >= 2) and np.abs(1 - max(pad_size / img_size)) > 0.02:
        overflow = (bg_size - img_size) // 2
        bg = bg[overflow[1]:, overflow[0]:][:img_size[1], :img_size[0]]
        axis = patches = None
        if pad_size[0] > 0:
            axis = 1
            patches = bg[:, :pad_size[0] // 2], bg[:, pad_size[0] // 2 - pad_size[0]:]
        elif pad_size[1] > 0:
            axis = 0
            patches = bg[:pad_size[1] // 2], bg[pad_size[1] // 2 - pad_size[1]:]
        if patches:
            r = max(20 / max(pad_size), 200 / min(img_size))
            patches = tuple(map(
                lambda x: cv2.resize(
                    cv2.GaussianBlur(
                        cv2.resize(x, None, None, r, r),
                        (11,) * 2, 0),
                    x.shape[1::-1]),
                patches))
        fg = np.concatenate((patches[0], fg, patches[1]), axis=axis)
    elif np.any(pad_size):
        fg = cv2.resize(fg, img_size)
    return fg


def _parse_img_size(value: str):
    if "," in value:
        parts = value.split(",")
        return tuple(int(p.strip()) for p in parts)
    return int(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image with blurred border")
    parser.add_argument("--src", type=Path, required=True, help="Source image file path")
    parser.add_argument("--img-size", type=str, default=None, help="Target image size (int or 'W,H')")
    parser.add_argument("--aspect-ratio", type=float, default=None, help="Target aspect ratio")
    args = parser.parse_args()

    src = cv2.imread(str(args.src))
    if src is None:
        raise RuntimeError(f"Failed to load image: {args.src}")
    img_size = _parse_img_size(args.img_size) if args.img_size else None
    result = make_blurred_border(src=src, img_size=img_size, aspect_ratio=args.aspect_ratio)
    output_path = args.src.parent / f"{args.src.stem}_bordered.png"
    cv2.imwrite(str(output_path), result)
    print(f"Saved: {output_path}")
