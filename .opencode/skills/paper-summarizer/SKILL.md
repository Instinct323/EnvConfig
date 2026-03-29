---
name: paper-summarizer
description: Summarize academic papers with strict evidence isolation. Use when user mentions papers, PDFs, arXiv, research papers, literature review, or cross-paper analysis.
---

# Paper Summarizer

Generate structured reports from academic papers. Supports single-paper deep dives and multi-paper comparative analysis.

## Core Principles

1. **Evidence first**: Read downloaded PDF before writing any summary.
2. **Full transcription**: `source.txt` must be complete plain text of `source.pdf`, not summary or excerpt.
3. **Schema order**: Emit report sections in the exact order defined in `schema.md`.
4. **No metadata-only summaries**: Never summarize from title/abstract alone.
5. **Citation safety**: Never use citation index (`[n]`) as paper title without verified mapping.
6. **Atomic registry**: Update `registry.json` in the same step as any file change.

## Registry Contract

Location: `.sisyphus/evidence/<run-id>/registry.json`

```json
{
  "<short-title>": {
    "repo": "url|none|\"\"",
    "pdf": "path|none|\"\"",
    "txt": "path|none|\"\"",
    "report": "path|none|\"\""
  }
}
```

**Value semantics**:

- `""` (empty): Not processed yet (default)
- `none`: Searched but not found
- Path/URL: Found and persisted

## Required Artifacts

Per-paper directory: `.sisyphus/evidence/<run-id>/<short-title>/`

| Artifact     | Required | Description                        |
|--------------|----------|------------------------------------|
| `source.pdf` | Yes      | Downloaded PDF                     |
| `source.txt` | Yes      | Full plain-text transcription      |
| `report.md`  | Yes      | Structured summary per `schema.md` |

## Workflow

### Step 1: Bootstrap

Create `registry.json` with all papers initialized to `""`.

```bash
python <skill-dir>/scripts/init_registry.py <run-id> --papers paper1 paper2
```

**Gate**: Registry parseable, all entries initialized.

### Step 2: Acquire

One delegated task per paper (`quick` agent):

1. Download PDF → `source.pdf`
2. Extract full text → `source.txt`
3. Find repository URL
4. Update registry fields

**Validation** (separate verifier agent):

```bash
# Verify single paper
python <skill-dir>/scripts/check_source.py <run-id> --paper <short-title>

# Verify all papers (at step end)
python <skill-dir>/scripts/check_source.py <run-id>
```

**Gate**: Exit code 0, PDF+TXT exist, TXT is full transcription (not summary), registry synced.

### Step 3: Report

One delegated task per paper (`ultrabrain` agent):

1. Read `<skill-dir>/schema.md` for section order
2. Read downloaded PDF
3. Generate `report.md` following schema
4. Update registry

**Validation** (separate verifier agent):

```bash
# Verify single paper
python <skill-dir>/scripts/check_report.py <run-id> --paper <short-title>

# Verify all papers (at step end)
python <skill-dir>/scripts/check_report.py <run-id>
```

**Gate**: Exit code 0, schema order correct, PDF read before summary, claims grounded in PDF content.

### Step 4: Finalize

Produce final output:

```bash
python <skill-dir>/scripts/final_report.py <run-id>
```

**Single paper**: Return `report.md` path directly.  
**Multiple papers**: Merge reports and add Cross-Paper Analysis section.

**Gate**:

- Multi-paper: merge provenance includes input paths + merge order + output path
- Registry synced with all artifacts
- No files outside run directory

## Verdict

| Result    | Condition                                  |
|-----------|--------------------------------------------|
| `APPROVE` | All steps PASS (exit code 0) or NA allowed |
| `REJECT`  | Any step fails (non-zero exit)             |

## Common Failures

- Missing `source.pdf`, `source.txt`, or `report.md`
- `source.txt` is summary/excerpt instead of full PDF transcription
- Summarized without reading downloaded PDF
- Step 2/3 executed without running validation scripts
- Multi-paper merge lacks provenance information
- Artifacts written outside `.sisyphus/evidence/<run-id>/`
- Registry out of sync with actual files
