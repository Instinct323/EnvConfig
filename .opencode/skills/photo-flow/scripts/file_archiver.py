from __future__ import annotations

import argparse
import math
import shutil
import time
from pathlib import Path

from tqdm import tqdm


def parse_txt_cfg(file, encoding="utf-8", comments="#"):
    with open(file, encoding=encoding) as f:
        for i_line in enumerate(s.split(comments)[0].strip() for s in f.read().splitlines()):
            if i_line[1]:
                yield i_line


class FileArchiver:
    def __init__(self,
                 txt_cfg: str | Path,
                 dst: str | Path,
                 file_fmt: str = "%i-%n",
                 reverse: bool = False):
        txt_cfg = Path(txt_cfg)
        assert txt_cfg.is_file(), "Invalid configuration file."
        self.dst = Path(dst) / f"{__class__.__name__}-{time.strftime('%Y%m%d%H%M%S')}"
        self.dst.mkdir(parents=True)
        self.files: list[Path] = []
        self.include(txt_cfg)
        if reverse:
            self.files.reverse()
        ndigit = math.ceil(math.log10(len(self.files)))
        with (self.dst / ".archive.txt").open("w") as fi:
            for i, f in enumerate(tqdm(self.files, desc="Archiving")):
                fi.write(str(f) + "\n")
                name = file_fmt.replace("%n", f.stem).replace("%i", str(i).zfill(ndigit))
                shutil.copy(f, self.dst / (name + f.suffix))

    def include(self, txt_cfg):
        root = Path(txt_cfg.parent).resolve()
        for i, line in parse_txt_cfg(txt_cfg):
            if line.startswith("@"):
                k, v = line[1:].split("=")
                if k == "include":
                    self.include(root / (v + ".txt"))
                elif k == "root":
                    root = (txt_cfg.parent / v).resolve()
            else:
                f = root / line
                self.files.append(f) if f.is_file() else (
                    print(f"File \"{txt_cfg}\", line {i + 1}: \"{f}\" does not exist."))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File archiving manager")
    parser.add_argument("--txt-cfg", type=Path, required=True, help="Configuration file path")
    parser.add_argument("--dst", type=Path, required=True, help="Destination directory path")
    parser.add_argument("--file-fmt", type=str, default="%i-%n", help="File name format (default: %i-%n)")
    parser.add_argument("--reverse", action="store_true", help="Reverse file order")
    args = parser.parse_args()

    FileArchiver(txt_cfg=args.txt_cfg, dst=args.dst, file_fmt=args.file_fmt, reverse=args.reverse)
