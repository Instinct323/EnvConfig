from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np
import supervision as sv


def fsize_lim_save(img: np.ndarray, file: Path, fsize: int = 2 ** 20, eps: float = 1e-3, max_iter: int = 100):
    cv2.imwrite(str(file), img)
    org = file.stat().st_size
    assert fsize < org, f"File size is already less than the target size: {org}"

    capa_tar = 1 - eps / 2
    r_img = fsize * capa_tar / org
    capacity = [1]
    best = (0, None)

    for i in range(max_iter):
        tmp = sv.scale_image(img, min(2, r_img * capa_tar / capacity[-1]))
        r_img = tmp.shape[0] / img.shape[0]
        cv2.imwrite(str(file), tmp)
        capacity.append(file.stat().st_size / fsize)
        print(f"[INFO] Iteration {i}: \tcapacity = {capacity[-1]:.6f}, r_img = {r_img:.6f}")

        if capacity[-1] < 1:
            if capacity[-1] > best[0]:
                best = (capacity[-1], r_img)
            if capacity[-1] > 1 - eps:
                break

        if capacity[-1] in capacity[-3:-1]:
            capa_tar = 1 - eps * np.random.random()

    cv2.imwrite(str(file), sv.scale_image(img, best[1])[0])
    return best[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save image with file size limit")
    parser.add_argument("--src", type=Path, required=True, help="Input image file path")
    parser.add_argument("--dst", type=Path, required=True, help="Output image file path")
    parser.add_argument("--fsize", type=int, default=2 ** 20, help="Target file size in bytes (default: 1048576)")
    parser.add_argument("--eps", type=float, default=1e-3, help="Tolerance epsilon (default: 1e-3)")
    parser.add_argument("--max-iter", type=int, default=100, help="Maximum iterations (default: 100)")
    args = parser.parse_args()

    img = cv2.imread(str(args.src))
    if img is None:
        raise RuntimeError(f"Failed to load image: {args.src}")
    fsize_lim_save(file=args.dst, img=img, fsize=args.fsize, eps=args.eps, max_iter=args.max_iter)
