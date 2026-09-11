from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterator

import PyPDF2


def merge_pdf(src: Iterator[Path], dst: Path):
    merger = PyPDF2.PdfMerger()
    for f in src:
        try:
            merger.append(f)
        except Exception:
            print(f'Failed to merge "{f}"')
    merger.write(str(dst))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one")
    parser.add_argument("--src", type=Path, nargs="+", required=True, help="Source PDF file paths")
    parser.add_argument("--dst", type=Path, required=True, help="Destination PDF file path")
    args = parser.parse_args()

    merge_pdf(src=iter(args.src), dst=args.dst)
