from __future__ import annotations

import argparse
from pathlib import Path

from tqdm import tqdm


def pdf2img(input_file: Path, output: str, blowup=15):
    import pymupdf

    pdf = pymupdf.open(input_file)
    for i, page in tqdm(list(enumerate(pdf)), desc="pdf to image"):
        pix = page.get_pixmap(matrix=pymupdf.Matrix(blowup, blowup))
        output_path = Path(output.format(page=i + 1))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(output_path)
    pdf.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF pages to images")
    parser.add_argument("-i", "--input", type=Path, required=True, help="Input PDF file path")
    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Output filename template, e.g. 'folder/{page}.png'")
    parser.add_argument("--scale", type=int, default=15,
                        help="Image resolution scale factor (default: 15)")
    args = parser.parse_args()

    pdf2img(input_file=args.input, output=args.output, blowup=args.scale)
