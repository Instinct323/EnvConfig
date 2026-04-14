import argparse
from pathlib import Path

import cv2
import numpy as np


def remove_background(img: np.ndarray, color_bg: int | tuple, thresh: int = 10) -> np.ndarray:
    mask = np.abs(img.astype(int) - color_bg).sum(axis=-1) >= thresh
    alpha = mask.astype(np.uint8) * 255
    return np.concatenate([img, alpha[..., None]], axis=-1)


def _parse_color_bg(value: str) -> int | tuple:
    if "," in value:
        parts = value.split(",")
        return tuple(int(p.strip()) for p in parts)
    return int(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove background from image")
    parser.add_argument("--img", type=Path, required=True, help="Input image file path")
    parser.add_argument("--color-bg", type=str, required=True, help="Background color (int or 'R,G,B' tuple)")
    parser.add_argument("--thresh", type=int, default=10, help="Threshold for background detection (default: 10)")
    args = parser.parse_args()

    img = cv2.imread(str(args.img))
    if img is None:
        raise RuntimeError(f"Failed to load image: {args.img}")
    color_bg = _parse_color_bg(args.color_bg)
    result = remove_background(img=img, color_bg=color_bg, thresh=args.thresh)

    output_path = args.img.parent / f"{args.img.stem}_nobg.png"
    cv2.imwrite(str(output_path), result)
    print(f"Saved: {output_path}")
