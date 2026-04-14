---
name: file-process
description: File conversion and processing. Trigger when user needs PDF-to-image conversion, PDF merging, image compression, background removal, or video I/O.
---

# File Process

Scripts in `<skill-dir>/scripts/`:

- `pdf2img.py` - Convert PDF to images
- `fsize_lim_save.py` - Compress image to target file size
- `merge_pdf.py` - Merge PDF files
- `remove_background.py` - Remove image background

Run scripts with `--help` for usage details.

For video I/O, use `supervision` library:

```python
import supervision as sv
help(sv.VideoSink)
help(sv.VideoInfo)
```