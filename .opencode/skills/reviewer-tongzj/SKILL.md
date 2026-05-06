---
name: reviewer-tongzj
description: Multi-agent review system for code and writing quality. Orchestrates parallel reviews across different dimensions - naming, structure, AI artifacts, academic style. Use when user needs comprehensive review, quality assessment, or when applying multiple quality standards simultaneously.
license: MIT
---

# Reviewer-TongZJ: Multi-Agent Review System

**Architecture**: Parallel specialized agents, each focusing on one quality dimension.

**IMPORTANT - For Maintainers:**
This skill integrates content from `karpathy-guidelines`. When refactoring:
1. Always re-reference the current version of `karpathy-guidelines`
2. Ensure key principles are preserved: Think Before Acting, Simplicity First, Surgical Changes, Goal-Driven Execution

---

## Table of Contents

1. [Quick Start](#1-quick-start)
   - 1.1 [Code Review Example](#11-code-review-example)
   - 1.2 [Writing Review Example](#12-writing-review-example)
2. [Code Review Agents](#2-code-review-agents)
   - 2.1 [Core Principles (Karpathy)](#21-core-principles-karpathy)
   - 2.2 [Agent Selection Guide](#22-agent-selection-guide)
   - 2.3 [Naming Reviewer](#23-naming-reviewer)
   - 2.4 [Structure Reviewer](#24-structure-reviewer)
   - 2.5 [AI Artifact Reviewer](#25-ai-artifact-reviewer)
   - 2.6 [Architecture Reviewer](#26-architecture-reviewer)
3. [Writing Review Agents](#3-writing-review-agents)
   - 3.1 [Clarity Reviewer](#31-clarity-reviewer)
   - 3.2 [Academic Style Reviewer](#32-academic-style-reviewer)
4. [Multi-Round Review Process](#4-multi-round-review-process)
   - 4.1 [Phase 1: Identify Changed Content](#41-phase-1-identify-changed-content)
   - 4.2 [Phase 2: Parallel Specialist Review](#42-phase-2-parallel-specialist-review)
   - 4.3 [Phase 3: Critical Review](#43-phase-3-critical-review)
   - 4.4 [Phase 4: Consolidated Fix & Verification](#44-phase-4-consolidated-fix--verification)
5. [Output Format Standards](#5-output-format-standards)
   - 5.1 [Individual Agent Output](#51-individual-agent-output)
   - 5.2 [Summary Report](#52-summary-report)
6. [Quick Reference](#6-quick-reference)
7. [Appendix](#7-appendix)

---

## 1. Quick Start

### 1.1 Code Review Example

Spawn 4 parallel agents for comprehensive code review:

```typescript
task(category="quick", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Naming review: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Structure review: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="AI artifact removal: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Architecture review: [files]")
```

### 1.2 Writing Review Example

Spawn 3 parallel agents for document review:

```typescript
task(category="quick", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Clarity review: [document]")
task(category="quick", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Academic style review: [document]")
task(category="deep", load_skills=["reviewer-tongzj"], run_in_background=true,
     prompt="Coherence review: [document]")
```

---

## 2. Code Review Agents

### 2.1 Core Principles (Karpathy)

These principles apply to all code reviews:

#### Principle 1: Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

#### Principle 2: Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

#### Principle 3: Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

#### Principle 4: Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

### 2.2 Agent Selection Guide

| Task Type | Agents to Spawn | Category |
|-----------|----------------|----------|
| Python code | Naming + Structure + AI Artifact + Architecture | quick/quick/quick/deep |
| Web/TS code | Naming + Structure + AI Artifact + Architecture | quick/quick/quick/deep |
| Mixed content | All relevant agents | varies |

### 2.3 Naming Reviewer

**Focus**: Variable, function, class naming conventions

**Standards**

Short names (common objects):
```
pcd, cfg, T, R, vec, req, fp
```

Descriptive names (domain concepts):
```
Tcw (camera to world), Teb (end effector to base)
len_finger, radius_mesh
```

**Convention Table:**

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case, short | `pcd`, `cfg`, `Tcw` |
| Functions | snake_case | `solve_v2v()` |
| Classes | PascalCase | `TwoFingerGripper` |
| Constants | UPPER_SNAKE | `MAX_RESULTS = 10` |
| Private | _leading | `_compute_pos()` |

**Anti-Patterns to Flag**
- Verbose names: `point_cloud_data` → should be `pcd`
- Inconsistent casing within same scope
- Ambiguous abbreviations without context

**Review Prompt Template**
```
Review [files] for naming standards:
- Variables: snake_case, short (pcd, cfg, Tcw)
- Functions: snake_case (solve_v2v)
- Classes: PascalCase (TwoFingerGripper)
- Constants: UPPER_SNAKE
- Domain concepts: descriptive (Tcw, len_finger)

Flag: verbose names, inconsistent casing, ambiguous abbreviations
Output format: [Line X] [Current] → [Suggested] ([Reason])
```

### 2.4 Structure Reviewer

**Focus**: Code organization, nesting depth

**Standards**

Function structure:
- Small functions, single purpose
- Max 2-3 nesting levels
- Type hints: use but not verbose
- 2 blank lines between top-level defs
- 1 blank line between methods

**Anti-Patterns to Flag**
- Functions >50 lines
- Nesting >3 levels
- Missing blank lines between defs

**Review Prompt Template**
```
Review [files] for structure standards:
- Function size: max 50 lines, single purpose
- Nesting depth: max 3 levels
- Blank lines: 2 between top-level, 1 between methods

Flag: large functions, deep nesting
Output format: [File:Line] [Issue] → [Suggestion]
```

### 2.5 AI Artifact Reviewer

**Focus**: Remove AI-generated code smells while preserving functionality

**Standards**

**NEVER Remove (Functional Code):**
- Comments explaining intent (not action)
- Error handling for realistic edge cases
- Code that adds clarity
- Functional logic and business rules
- Type hints and validations
- Import statements (unless unused)

**ALWAYS Remove (AI Slops):**
- Obvious comments: `# increment i`, `# loop through items`
- Comments that state the obvious: `# check if valid`
- Over-defensive code: unnecessary try-except for impossible cases
- Verbose error handling for scenarios that cannot occur
- Boilerplate that's not serving a purpose
- Speculative abstractions for single-use code
- "Flexibility" or "configurability" that wasn't requested

**Quality Assurance Rules**

**CRITICAL - Safety First:**
- NEVER remove code that serves a functional purpose
- ALWAYS verify changes compile/parse correctly
- ALWAYS preserve test coverage
- If uncertain about a change, err on the side of keeping the original code

**Behavior Preservation:**
- Return values must remain unchanged
- Side effects must remain unchanged
- Exception behavior must remain unchanged
- Edge case handling must be preserved

**Review Prompt Template**

```
Remove AI artifacts from [files]:

## Phase 1: Identify AI Slops
Scan for and flag:
- [ ] Obvious comments (# increment i, # loop through items)
- [ ] Over-defensive error handling (try-except for impossible cases)
- [ ] Speculative abstractions (unused flexibility/configurability)
- [ ] Boilerplate not serving a purpose
- [ ] Comments stating the obvious

## Phase 2: Safety Verification
For each flagged item:
- [ ] Does this serve a functional purpose? → KEEP
- [ ] Is this realistic error handling? → KEEP
- [ ] Does this explain intent (not action)? → KEEP
- [ ] Is this genuinely AI slop? → REMOVE

## Phase 3: Apply Changes
Remove confirmed AI slops only. Document each removal.

Output format:
### Removed
- [File:Line] [Artifact type] - [Reason for removal]

### Kept (Functional)
- [File:Line] [Item] - [Reason for keeping]

### Verification
- [ ] All changes compile/parse correctly
- [ ] No functional logic removed
- [ ] Test coverage preserved
```

### 2.6 Architecture Reviewer

**Focus**: Code quality, anti-patterns, surgical changes

**Quality Gates**

**MUST PASS:**
- No dead code (unused imports, functions, variables)
- No CSS var forwarding chains
- No default fallbacks hiding errors
- Comments: English only, minimal, intent-focused
- Tests: minimal and stable

**Anti-Patterns:**
1. Chinese comments
2. Magic numbers (use constants)
3. Long parameter lists (>5 params)
4. CSS `var()` with fallback values
5. Refactoring things that aren't broken

**Review Prompt Template**
```
Deep review of [files] for architecture:
- Dead code: unused imports, functions, variables
- Anti-patterns: magic numbers, long param lists, var fallbacks
- Surgical changes: only necessary edits, style consistency
- Quality: no CSS forwarding, fail-fast configs, minimal comments

Flag: dead code, anti-patterns, unnecessary changes
Output format: [Severity] [File:Line] [Issue] → [Fix] ([Principle])
```

---

## 3. Writing Review Agents

### 3.1 Clarity Reviewer

**Focus**: Remove AI flavor, improve directness

**Standards**

**Avoid AI-flavored phrases:**
- "specifically", "in summary", "as mentioned above"
- "it is worth noting that", "interestingly", "importantly"

**Avoid vague modifiers:**
- "to a large extent", "very", "extremely" (without data)
- "obviously", "clearly" (if obvious, don't state it)

**Prefer:**
- Direct statements over circuitous expressions
- Remove redundancy
- Paragraphs, not one-sentence-per-line

**Review Prompt Template**
```
Review [document] for clarity:
- Remove AI-flavored phrases (specifically, in summary, etc.)
- Eliminate vague modifiers without substance
- Check for redundancy (saying same thing twice)
- Ensure paragraph structure (not bullet lists)

Output format: [Section] [Issue] → [Suggested revision]
```

### 3.2 Academic Style Reviewer

**Focus**: Academic writing conventions

**Standards**

**Citation & terminology:**
- Define abbreviations on first use
- Use Fig. / Tab. (not Figure / Table)
- Follow domain conventions

**Formatting:**
- Avoid bold in running text
- Consistent section hierarchy
- Proper table formatting

**Review Prompt Template**
```
Review [document] for academic style:
- Abbreviations: defined on first use, consistent thereafter
- Citations: Fig./Tab. not Figure/Table
- Formatting: no bold in text, consistent hierarchy
- Domain-specific conventions followed

Output format: [Location] [Style issue] → [Correction]
```

---

## 4. Multi-Round Review Process

A structured 4-phase review workflow.

### 4.1 Phase 1: Identify Changed Content

**Scope Detection:**
- Determine review scope (files, modules, or entire codebase)
- For branch review: Identify files changed vs base branch
- For code review: Identify modified functions/classes
- For document review: Identify changed sections

**Preparation:**
- Save rollback artifacts (per-file patches) before making changes
- Ensure test coverage exists for modified code
- Document baseline behavior for verification

### 4.2 Phase 2: Parallel Specialist Review

Spawn all relevant agents simultaneously for comprehensive analysis.

**Collect all feedback**, aggregate issues by file/section.

### 4.3 Phase 3: Critical Review

After all specialist agents complete, perform critical review with the following checklist:

#### Safety Verification
- [ ] No functional logic was accidentally removed
- [ ] All error handling is preserved
- [ ] Type hints remain correct and complete
- [ ] Import statements are still valid
- [ ] No breaking changes to public APIs

#### Behavior Preservation
- [ ] Return values unchanged
- [ ] Side effects unchanged
- [ ] Exception behavior unchanged
- [ ] Edge case handling preserved

#### Code Quality
- [ ] Removed changes are genuinely AI slop (not intentional patterns)
- [ ] Remaining code follows project conventions
- [ ] No orphaned code or dead references
- [ ] All changes compile/parse correctly

### 4.4 Phase 4: Consolidated Fix & Verification

**Apply fixes based on aggregated feedback:**
1. Group related issues by category
2. Apply surgical changes (one category at a time)
3. Re-verify after each category of fix
4. Use rollback artifacts if issues are found

**Final Verification Checklist:**
- [ ] All flagged issues addressed?
- [ ] No new issues introduced?
- [ ] Style consistency maintained?
- [ ] Success criteria met?
- [ ] All changes compile/parse correctly?
- [ ] Tests pass (if applicable)?

---

## 5. Output Format Standards

All agents should use consistent output for individual reviews.

### 5.1 Individual Agent Output

```
## Review: [Agent Type] - [File/Document]

### Summary
- Total issues: [N critical, N warnings, N suggestions]
- Time spent: [X minutes]

### Issues by Category

**[Category 1]**
- [Severity] [Location] [Current] → [Suggested] ([Principle])
  - Explanation: [Why this matters]

**[Category 2]**
...

### Action Items
- [ ] [Priority] Fix [specific issue]
- [ ] [Priority] Address [category of issues]

### Positive Findings
- [What was done well]
```

### 5.2 Summary Report

After completing all phases, generate a consolidated summary:

```
## Review Summary Report

### Files/Documents Processed
- file1.py: X issues found, Y fixed
- file2.ts: X issues found, Y fixed
- document.md: X issues found, Y fixed

### Critical Review Results
- **Safety**: PASS / FAIL / PARTIAL
  - [Details if failed]
- **Behavior Preservation**: PASS / FAIL / PARTIAL
  - [Details if failed]
- **Code Quality**: PASS / FAIL / PARTIAL
  - [Details if failed]

### Issues by Category

**AI Artifacts**
- N obvious comments removed
- N over-defensive error handlers removed
- N speculative abstractions eliminated

**Naming**
- N verbose names shortened
- N inconsistent casing fixed

**Structure**
- N large functions flagged
- N deep nesting issues found

**Architecture**
- N dead code instances removed
- N anti-patterns flagged

### Issues Found & Fixed
1. [Issue description] → [Fix applied]
2. [Issue description] → [Fix applied]

### Final Status
[ ] CLEAN - No issues found
[ ] ISSUES FIXED - All identified issues resolved
[ ] REQUIRES ATTENTION - Some issues remain, manual review needed

### Rollback Information
- Rollback artifacts saved at: [location]
- Use rollback if: [conditions]
```

---

## 6. Quick Reference

### 6.1 Agent Selection Quick Reference

| Task Type | Agents to Spawn | Category |
|-----------|----------------|----------|
| Python code | Naming + Structure + AI Artifact + Architecture | quick/quick/quick/deep |
| Web/TS code | Naming + Structure + AI Artifact + Architecture | quick/quick/quick/deep |
| Academic paper | Clarity + Academic Style | quick/quick |
| Documentation | Clarity + Structure (if code examples) | quick/quick |
| Mixed content | All relevant agents | varies |

---

## 7. Appendix

### Update Log

- v1.0: Initial coder-tongzj skill
- v2.0: Added writing standards
- v3.0: Renamed to reviewer-tongzj, integrated Karpathy guidelines
- v4.0: Re-architected as multi-agent review system with specialized reviewers
- v5.0: Optimized table of contents - moved Karpathy principles into Code Review section
