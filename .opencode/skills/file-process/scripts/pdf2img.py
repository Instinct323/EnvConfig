import argparse
from pathlib import Path
from tqdm import tqdm


def pdf2img(file: Path, suffix=".png", root="Project", blowup=15):
    import fitz

    root = file.parent / root
    if not root.is_dir():
        root.mkdir()

    pdf = fitz.open(file)
    for i, page in tqdm(list(enumerate(pdf)), desc="pdf to image"):
        pix = page.get_pixmap(matrix=fitz.Matrix(blowup, blowup))
        pix.save(root / (file.stem + f"-{i + 1}{suffix}"))
    pdf.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF pages to images")
    parser.add_argument("--file", type=Path, required=True, help="Path to the PDF file")
    parser.add_argument("--suffix", type=str, default=".png", help="Image file suffix (default: .png)")
    parser.add_argument("--root", type=str, default="Project", help="Output directory name (default: Project)")
    parser.add_argument("--blowup", type=int, default=15, help="Image resolution blowup factor (default: 15)")
    args = parser.parse_args()

    pdf2img(file=args.file, suffix=args.suffix, root=args.root, blowup=args.blowup)
