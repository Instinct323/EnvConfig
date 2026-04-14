import argparse
from pathlib import Path
from typing import Callable, Iterable

from tqdm import tqdm

import numpy as np


def star_trails_video(src: Iterable[np.ndarray],
                      decay: float = 0.99,
                      agg_fun: Callable = np.maximum):
    assert 0 < decay <= 1
    src = iter(tqdm(src))

    cur = next(src)
    yield cur
    cur = cur.astype(np.float32)

    for img in map(np.float32, src):
        cur = agg_fun(cur * decay, img)
        yield np.round(cur).astype(np.uint8)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create star trails video")
    parser.add_argument("--src", type=Path, required=True, help="Source directory containing images")
    parser.add_argument("--decay", type=float, default=0.99, help="Brightness decay factor (default: 0.99)")
    parser.add_argument("--agg-fun", type=str, choices=["maximum", "minimum"], default="maximum",
                        help="Aggregation function (default: maximum)")
    args = parser.parse_args()

    agg_fun_map = {"maximum": np.maximum, "minimum": np.minimum}
    agg_fun = agg_fun_map[args.agg_fun]

    import cv2

    image_files = sorted([f for f in args.src.iterdir() if f.suffix.lower() in (".jpg", ".jpeg", ".png")])
    images = [cv2.imread(str(f)) for f in image_files]
    images = [img for img in images if img is not None]

    for i, frame in enumerate(star_trails_video(src=images, decay=args.decay, agg_fun=agg_fun)):
        output_path = args.src.parent / f"frame_{i:04d}.png"
        cv2.imwrite(str(output_path), frame)
    print(f"Saved frames to: {args.src.parent}")
