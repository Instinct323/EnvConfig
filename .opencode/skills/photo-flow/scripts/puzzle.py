from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np

logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)
LOGGER = logging.getLogger("utils")


@dataclass
class NumString:
    length: int = 8
    step: int = 5

    def __iter__(self):
        for i in range(0, 10 ** self.length, self.step):
            yield str(i).zfill(self.length)


class Puzzle:

    def __init__(self,
                 img: Path,
                 material: Path,
                 shape: tuple = (2, 3),
                 dpi: int = 1280,
                 pad_width: float = 0.05,
                 pad_value: int = 255):
        self.stride = dpi
        self.cells = self.partition(img, shape)
        self.pad_kwarg = dict(borderType=cv2.BORDER_CONSTANT,
                              value=[pad_value] * 3 if isinstance(pad_value, int) else pad_value)
        self.pad_size = np.round(np.array([pad_width, pad_width / 2]) / 2 * self.stride).astype(np.int32)
        self.material = self.parse_material(material)
        self.puzzle()

    def imread(self, file, warn_only=True):
        img = cv2.imread(str(file))
        check = img is not None
        if not check:
            msg = f"Unreadable image file: {file}"
            if warn_only:
                LOGGER.warning(msg)
            else:
                raise RuntimeError(msg)
        else:
            ksize = int(img.shape[1] / self.stride / 2) * 2 + 1
            if ksize >= 3:
                img = cv2.GaussianBlur(img, ksize=[ksize] * 2, sigmaX=1)
        return img, check

    def partition(self, img, shape):
        img = self.imread(img, warn_only=False)[0]
        img = cv2.resize(img, np.array(shape[::-1]) * self.stride)
        cells = sum(map(lambda x: np.split(x, shape[1], axis=1),
                        np.split(img, shape[0], axis=0)), [])
        return cells

    def parse_material(self, material):
        if material:
            material = [folder for folder in material.iterdir() if folder.is_dir()]
            assert len(material) == len(self.cells), f"The number of material packs should be {len(self.cells)}"
            w = self.stride - 2 * self.pad_size[0]
            for i in np.arange(len(material)):
                orders = iter(NumString())
                folder, material[i] = material[i], []
                for file in folder.iterdir():
                    j = Path()
                    while j.exists():
                        j = file.parent / f"{next(orders)}{file.suffix}"
                    file = file.rename(j)
                    img, check = self.imread(file)
                    if check:
                        h = round(img.shape[0] / img.shape[1] * w)
                        img = cv2.resize(img, [w, h])
                        img = cv2.copyMakeBorder(img, *self.pad_size.repeat(2)[::-1], **self.pad_kwarg)
                        material[i].append(img)
                LOGGER.info(f"The material package {i + 1} is loaded")
        return material

    def puzzle(self):
        concat = lambda x: np.concatenate(x, axis=0) if x else np.array([])
        pad_vert = lambda x, bottom, top: (
            cv2.copyMakeBorder(x, bottom=bottom, top=top, left=0, right=0, **self.pad_kwarg)) \
            if x.size else np.full((bottom + top, self.stride, 3), 255, dtype=np.uint8)

        for i, cell in enumerate(self.cells):
            img_queue = self.material[i]
            if img_queue:
                img_h = np.array([img.shape[0] for img in img_queue], dtype=np.float32)
                loc_bottom = np.cumsum(img_h)
                length = len(img_queue)
                loss = np.abs(loc_bottom / loc_bottom[-1] - 0.5) * \
                       (1 + np.abs(np.arange(length) + 0.5 - length / 2))
                ctr = loss.argmin() + 1
                img_queue = img_queue[:ctr], img_queue[ctr:]
                img_queue = list(map(concat, img_queue))
                max_h = max(j.shape[0] for j in img_queue)
                img_queue[0] = pad_vert(img_queue[0], bottom=0, top=max_h - img_queue[0].shape[0] + self.pad_size[1])
                img_queue[1] = pad_vert(img_queue[1], bottom=max_h - img_queue[1].shape[0] + self.pad_size[1], top=0)
                cell = pad_vert(cell, bottom=self.pad_size[1] * 4, top=self.pad_size[1] * 4)
                img_queue.insert(1, cell)
                cell = np.concatenate(img_queue)
            cv2.imwrite(f"{i + 1}_puzzle.png", cell)
            LOGGER.info(f"The part {i + 1} has been saved as {i + 1}_puzzle.png")
        LOGGER.info(f"The generated image has been saved in {Path.cwd()}")


def _parse_shape(value: str) -> tuple:
    parts = value.split(",")
    return tuple(int(p.strip()) for p in parts)


def _parse_pad_value(value: str):
    if "," in value:
        parts = value.split(",")
        return tuple(int(p.strip()) for p in parts)
    return int(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create puzzle effect from image and materials")
    parser.add_argument("--img", type=Path, required=True, help="Foreground image file path")
    parser.add_argument("--material", type=Path, required=True, help="Material package directory path")
    parser.add_argument("--shape", type=str, default="2,3", help="Grid shape as 'W,H' (default: 2,3)")
    parser.add_argument("--dpi", type=int, default=1280, help="Output image width (default: 1280)")
    parser.add_argument("--pad-width", type=float, default=0.05, help="Side padding ratio (default: 0.05)")
    parser.add_argument("--pad-value", type=str, default="255", help="Padding value (int or 'R,G,B')")
    args = parser.parse_args()

    shape = _parse_shape(args.shape)
    pad_value = _parse_pad_value(args.pad_value)
    Puzzle(img=args.img, material=args.material, shape=shape, dpi=args.dpi,
           pad_width=args.pad_width, pad_value=pad_value)
