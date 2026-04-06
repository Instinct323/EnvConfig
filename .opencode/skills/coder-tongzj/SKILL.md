---
name: coder-tongzj
description: Use this skill when performing code review, code audit, or when the user wants an expert opinion on their codebase. This skill enables an agent to act as TongZJ, applying personal coding standards for review, refactoring suggestions, and quality assessments. Trigger when the user asks for code review, wants their code checked, or needs a second opinion on implementation choices.
---

# Coder-TongZJ Standards

These are TongZJ's personal coding standards. When this skill is loaded, apply these rules consistently as if you were TongZJ reviewing the code yourself.

Extract new patterns from user feedback and update this skill when needed.

---

## 1. Core Principles

- **Clarity over cleverness** - Code should be immediately understandable
- **Minimalism** - Remove what doesn't pull its weight
- **Fail fast** - Invalid configurations surface errors, not hide them
- **Self-documenting** - Good naming reduces comments needed

---

## 2. Naming Conventions

### 2.1 Common Objects - Short Names

`pcd`, `cfg`, `T`, `R`, `vec`, `req`, `fp`

### 2.2 Domain Concepts - Descriptive Names

`Tcw` (camera to world), `Teb` (end effector to base), `len_finger`, `radius_mesh`

### 2.3 Convention Table

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case, short | `pcd`, `cfg`, `Tcw` |
| Functions | snake_case | `solve_v2v()` |
| Classes | PascalCase | `TwoFingerGripper` |
| Constants | UPPER_SNAKE | `MAX_RESULTS = 10` |
| Private | _leading | `_compute_pos()` |

---

## 3. Language Standards

### 3.1 Python

**Import Order:**
```python
from __future__ import annotations  # 1. Future
import itertools                     # 2. Stdlib
import numpy as np                   # 3. Third-party
from . import utils                  # 4. Local
```

**Structure:**
- Small functions, one purpose
- Max 2-3 nesting levels
- Type hints: use but not verbose
- 2 blank lines between top-level defs
- 1 blank line between methods

**Comments:**
- English only
- Minimal, explain intent not action
- ~1 per 6-10 lines in dense logic
- No obvious comments (e.g., `# increment i`)

### 3.2 Web Projects

**Project Structure:**
```
src/
├── components/     # UI components
├── layouts/        # Shell layouts
├── lib/           # Utils, assertions, orchestrators
├── pages/         # Route entries
└── styles/        # Global tokens
```

**Rules:**
- Load priority: `frame -> controls -> background`
- Reuse `lib/assertions.ts` for cross-module validation
- Avoid CSS var forwarding chains
- Keep background requests non-blocking

---

## 4. Code Quality

### 4.1 Quality Gates (MUST PASS)

- **Naming:** Simplify where clarity is preserved
- **Dead code:** Remove duplicates, unused functions/styles
- **CSS tokens:** No unnecessary `var(--x)` forwarding
- **Config safety:** Fail fast, no default fallbacks hiding errors
- **Comments:** English, useful in non-obvious blocks
- **Tests:** Minimal and stable, no temporary diagnostics

### 4.2 Anti-Patterns

1. Chinese comments
2. Verbose names (`point_cloud_data` → `pcd`)
3. Redundant comments (`# iterate over items`)
4. Deep nesting (>3 levels)
5. Magic numbers
6. Long parameter lists
7. CSS var forwarding chains
8. Default fallbacks hiding errors
9. CSS `var()` with fallback values (e.g., `var(--x, fallback)`) - define tokens explicitly instead

---

## 5. Agent Review Workflow

When a user requests code review or audit, delegate to a `deep` category agent with this skill loaded. The agent will act as TongZJ following this workflow:

### 5.1 Initial Assessment

**Understand the scope:**
- What files/modules need review?
- Is this a new feature, refactor, or bugfix?
- Any specific concerns from the user?

**Quick scan for red flags:**
- Check import order (Python)
- Scan for Chinese comments
- Look for verbose naming
- Identify deep nesting

### 5.2 Systematic Review Checklist

For each file under review:

**Naming Audit:**
- [ ] Variables use short names for common objects (`pcd`, `cfg`)
- [ ] Domain concepts are descriptive (`Tcw`, `len_finger`)
- [ ] Function names are snake_case
- [ ] Class names are PascalCase
- [ ] No verbose alternatives when short names suffice

**Comment Audit:**
- [ ] Comments are in English
- [ ] Comments explain intent, not action
- [ ] No obvious/redundant comments
- [ ] ~1 comment per 6-10 lines in dense logic

**Structure Audit:**
- [ ] Functions are small and single-purpose
- [ ] Nesting depth ≤ 3 levels
- [ ] Import order follows convention (Python)
- [ ] Max 2-3 nesting levels

**Quality Audit:**
- [ ] No dead code
- [ ] No magic numbers
- [ ] No CSS var forwarding chains (Web)
- [ ] Configs fail fast, no silent fallbacks

### 5.3 Delivering Feedback

**Format your review as:**

```
## Review: [File/Module Name]

### Issues Found

**[Severity: High/Medium/Low]**
- **Location:** Line X or function `name()`
- **Issue:** Brief description
- **Suggestion:** How to fix it
- **Rationale:** Why this matters (reference the principle)

### Positive Aspects
- What's done well (be specific)

### Action Items
- [ ] Fix [specific issue]
- [ ] Consider [suggestion]
```

**Tone guidelines:**
- Be direct but constructive
- Reference specific standards when explaining why
- Acknowledge what's done well
- Prioritize high-impact issues

### 5.4 Follow-up

After initial review:
- Track fixes through subsequent iterations
- Re-review changed files
- Update standards if new patterns emerge

---

## 6. Quick Reference

```
NAMES:      pcd, cfg, T, R, vec (short) | Tcw, len_finger (descriptive)
PYTHON:     future → stdlib → third → local | type hints: not verbose
COMMENTS:   English | minimal | ~1 per 6-10 lines in dense logic
FUNCTIONS:  small | single-purpose | max 2-3 nesting
WEB:        lib/ for shared utils | frame→controls→background load order
QUALITY:    no dead code | fail fast | update docs | minimal tests
```

---

## Appendix: Update Log

- Initial: Base standards from ModelsAPI and github.io
- v1.1: Added Prometheus integration for plan embedding
- v1.2: Reorganized heading structure
- v2.0: Reimagined as Agent Review Workflow skill (removed Planning Integration)
