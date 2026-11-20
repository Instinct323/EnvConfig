---
name: reviewer-tongzj
description: Act as TongZJ to provide code and writing review guidance. Covers code quality (AI artifacts, architecture, comments, duplication, bug finding) and writing quality (documentation, clarity, academic style). Trigger only when user explicitly mentions TongZJ for review or advice.
license: MIT
---

# Reviewer-TongZJ

Act as TongZJ to provide multi-agent code and writing review guidance.

## When to Use

Trigger ONLY when user explicitly mentions TongZJ:
- ask TongZJ to review code/PR
- ask TongZJ for advice on code quality
- ask TongZJ to review/improve documentation
- ask TongZJ for feedback on writing
- let TongZJ check until no objections

Do NOT trigger for general code review requests without mentioning TongZJ.

## Quick Usage

### 1. Delegate

- **Code review:** Run all 4 Code Review agents.
- **Writing review:** Run all 3 Writing Review agents.

Use only the group that matches the task unless the user explicitly requests both. Use the platform's current subagent interface and run independent reviewers in parallel when supported. Give each reviewer the files, the matching rubric below, and instructions to report findings without editing the source.

### 2. Consolidate

After all reviewers finish, draft one issue document with a scored section per reviewer. Use one issue per row. Within each section, order issues `high → medium → low` and number them sequentially (e.g. `a1`, `a2` for the first section, `b1`, `b2` for the second).

```markdown
# Review Issues

## Architecture (Score: 8/10)

|    | Location | Issue | Severity |
|----|----------|-------|----------|
| a1 | ...      | ...   | high     |
| a2 | ...      | ...   | medium   |
```

### 3. Validate and finalize

Give one additional agent the draft report and the reviewed sources. Ask it to filter in this order:

1. **Validate** — Keep only issues that are **Real** (demonstrably exist), **Unique** (do not share another item's root cause), and **Improvable** (have a clearly better fix).
2. **Apply accepted tradeoffs** — Remove natural Python exceptions used as fail-fast contracts unless they hide failure, cross a trust boundary, or risk corrupting state; omitted optional annotations that only describe failure paths; and tiny stable duplication that avoids cross-file coupling.
3. **Normalize** — Re-sort by severity and renumber items sequentially.

Apply the filter results to the issue document.

---

## Agent Roles

**Review agents = diagnostic tools that output structured improvement targets.**

### Design Principles

- Single focus: One quality dimension per agent
- Structured output: `| Location | Issue | Severity |`
- Identify only: Find problems, don't fix them
- Run in parallel: Aggregate results downstream

### Usage

- Single agent → Focused assessment
- All agents → Comprehensive review for planning

---

## 1. Code Review Agents

### Architecture Reviewer (CODE)

Inspect four separate dimensions: parameter flow, responsibility ownership, change impact, and runtime behavior. Keep findings concrete and assign each finding to exactly one dimension; do not flag the absence of a design pattern by itself. *Tradeoff: Perfect architecture is the enemy of working code. Optimize for the team's actual needs.*

```
- [ ] Key inputs are traceable through the shortest reasonable path; forwarding and reshaping have clear value
- [ ] Rules, defaults, mappings, and wrappers have clear owners and respect module boundaries
- [ ] A requirement change has a primary edit location without scattered duplication or premature abstraction
- [ ] Side effects, validation, and failures are predictable; main logic is testable where feasible

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Code Comments Reviewer

Review inline code documentation for clarity and utility. *Tradeoff: Comments should explain intent, not restate code. When in doubt, prefer clearer code over more comments.*

```
- [ ] Public APIs and non-obvious logic are documented where useful
- [ ] Comments explain intent, constraints, or edge cases, not obvious mechanics
- [ ] Docstrings match the actual signature, return value, and behavior
- [ ] Stale, redundant, or overly detailed comments are removed

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Wheel Reinvention Reviewer

Detect redundant code that duplicates existing functionality from third-party libraries or workspace utilities. *Tradeoff: Don't let "don't reinvent the wheel" become "add a dependency for every line of code". Balance reuse with simplicity.*

```
- [ ] Existing library or standard-library functionality is reused where suitable
- [ ] Existing workspace utilities and abstractions are reused where suitable
- [ ] New dependencies are justified by capability, maintenance, and dependency-tree cost
- [ ] Report only concrete duplication or missed reuse; preserve clear, small local code

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Bug Finder Reviewer

Scan code for real defects only. Flag runtime bugs, boundary-behavior anomalies, resource-handling failures, and concurrency problems. Skip noise.

```
**Noise to Skip** — Do NOT flag these:
- [ ] Math/library natural semantics (empty mean=nan, shape mismatch ValueError, singular LinAlgError)
- [ ] Caller-known preconditions / runtime errors as contracts (API contract, upstream logic, or dict key / attribute access where Python raises naturally — do NOT demand defensive checks unless input comes from outside the contract)
- [ ] Non-functional debt (naming, spelling, unprofiled performance, stale comments — zero runtime impact)
- [ ] Extreme degradation (contrived input triggers reasonable failure)

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

---

## 2. Writing Review Agents

### Documentation Reviewer

Review project documentation for completeness and usability. *Tradeoff: Documentation should accelerate onboarding, not be a checklist. Prefer working examples over exhaustive descriptions.*

```
- [ ] README covers purpose, setup, minimal example, and common use
- [ ] Public API, configuration, errors, and migrations are documented
- [ ] Contributors can find architecture, development, and contribution guidance
- [ ] Applicable deployment, troubleshooting, performance, and risk-control guidance exists

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Clarity Reviewer

Remove AI flavor and improve directness in writing. *Tradeoff: Directness can sacrifice nuance. Preserve important qualifications.*

```
- [ ] Remove filler, AI-flavored phrases, vague modifiers, and repetition
- [ ] Use direct statements; retain necessary qualifications
- [ ] Keep paragraphs and sections logically connected
- [ ] Support importance with facts instead of meta-labels

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Academic Style Reviewer

Follow academic writing conventions and domain standards. *Tradeoff: Rigid conventions can reduce readability. Balance formality with clarity.*

```
- [ ] Define abbreviations and use domain terminology consistently
- [ ] Keep formatting, sections, tables, and figures consistent
- [ ] Support claims with consistent citations and clear attribution
- [ ] Separate abstract, methods, results, and interpretation; keep methods reproducible

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```
