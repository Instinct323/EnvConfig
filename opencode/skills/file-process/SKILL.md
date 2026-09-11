---
name: file-process
description: File conversion and processing. Trigger when user needs PDF-to-image conversion, PDF merging, image compression, background removal, video I/O, or markdown beautification.
---

# File Process

This skill provides two modes of file processing:

---

## Script-Based Processing

Use Python scripts in `<skill-dir>/scripts/` for automated processing.

### Available Scripts

| Script | Function | Usage Example |
|--------|----------|---------------|
| `pdf2img.py` | Convert PDF to images | `python pdf2img.py input.pdf --output-dir ./images` |
| `merge_pdf.py` | Merge PDF files | `python merge_pdf.py file1.pdf file2.pdf --output merged.pdf` |
| `fsize_lim_save.py` | Compress image to target size | `python fsize_lim_save.py input.jpg --target-size 500kb` |
| `remove_background.py` | Remove image background | `python remove_background.py input.png --output output.png` |

**For detailed usage:**
```bash
python <script-name> --help
```

### Video I/O

For video processing, use the `supervision` library:

```python
import supervision as sv

help(sv.VideoInfo)
help(sv.VideoSink)
```

---

## Markdown Beautification

Structure optimization and formatting beautification for Markdown documents.

### Core Principles

1. **Zero Content Changes** - Never modify any text content
2. **Manual Processing** - Markdown structure is unpredictable; handle case-by-case manually
3. **Structure Enhancement** - Add header numbering, convert lists to headers, etc.
4. **Code Formatting** - Wrap code examples in code blocks
5. **Quality Verification** - Check content integrity after processing
