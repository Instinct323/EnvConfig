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

**Select Agent Group based on task type, then spawn ALL agents in that group:**

### For Code Review

Run all 5 agents in Code Review group:
```typescript
task(category="quick", load_skills=["reviewer-tongzj"], prompt="AI Artifacts: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], prompt="Architecture (CODE): [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Code Comments: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], prompt="Wheel Reinvention: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Bug Finder: [files]")
```

### For Writing Review

Run all 3 agents in Writing Review group:
```typescript
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Documentation: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Clarity: [document]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Academic Style: [document]")
```

**Rule**: Only select ONE group based on the task type. Don't mix code and writing agents unless explicitly requested.

### Result Collection

After all agents complete, write the consolidated review results to an issue document with sequentially numbered items:

```markdown
# Review Issues

## AI Artifacts (Score: 7/10)

|    | Location | Issue | Severity |
|----|----------|-------|----------|
| a1 | ...

## Architecture (Score: 8/10)

|    | Location | Issue | Severity |
|----|----------|-------|----------|
| b1 | ...
```

---

## Agent Roles

**Review agents = diagnostic tools that output structured improvement targets.**

### Design Principles
- **Single focus**: One quality dimension per agent
- **Structured output**: `| Location | Issue | Severity |`
- **Identify only**: Find problems, don't fix them
- **Run in parallel**: Aggregate results downstream

### Usage
- **Single agent** → Focused assessment
- **All agents** → Comprehensive review for planning

---

## 1. Code Review Agents

### AI Artifact Reviewer

Remove AI-generated code smells while preserving functionality. *Tradeoff: When in doubt, keep the code. Safety over aggressive removal.*

```
**1. Intent Over Action** — Comment what you mean, not what you do.
- [ ] No obvious comments restating what code does
- [ ] Intent comments explaining "why" preserved
- [ ] Redundant comments removed

**2. Realistic Defense** — Handle errors that can actually happen.
- [ ] No over-defensive handling for impossible cases
- [ ] Realistic edge case handling preserved
- [ ] No silent defaults masking misconfiguration

**3. Justified Abstractions** — Abstract only when it serves a purpose.
- [ ] No speculative "flexibility" or "configurability"
- [ ] No forwarding wrappers without purpose
- [ ] Actual duplication-reducing abstractions kept
- [ ] Short code and single-use private functions inlined

**4. Clean Boilers** — Remove ceremony without function.
- [ ] No purposeless boilerplate
- [ ] Unused imports/variables/functions removed
- [ ] Functional code and clarity-adding code preserved

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Architecture Reviewer (CODE)

Analyze code maintainability from cognitive, change, and operational perspectives. *Tradeoff: Perfect architecture is the enemy of working code. Optimize for the team's actual needs.*

```
**1. Local Reasoning** — Understand a function without reading 10 other files.
- [ ] Functions/classes small and focused, with related logic colocated
- [ ] Nesting depth limited; no fragmented knowledge across overly granular files/modules
- [ ] No hidden side effects; prefer deep modules with simple interfaces
- [ ] Data flow explicit through parameters

**2. Stable Dependencies** — Depend on abstractions, not concretions.
- [ ] High-level modules independent of low-level details
- [ ] No circular dependencies; clean module seams without leakage
- [ ] Framework isolated from business logic
- [ ] Interfaces owned by consumers (DIP)

**3. Single Point of Change** — One requirement change touches one place.
- [ ] No duplicated code
- [ ] Configuration externalized
- [ ] Features encapsulated, not scattered
- [ ] Extensible without modification

**4. Observable Failures** — Bugs reveal themselves quickly with context.
- [ ] Fail fast with clear messages
- [ ] Error context preserved
- [ ] Defensive boundaries at edges
- [ ] Testable interfaces at appropriate locality

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Code Comments Reviewer

Review inline code documentation for clarity and utility. *Tradeoff: Comments should explain intent, not restate code. When in doubt, prefer clearer code over more comments.*

```
**1. Coverage** — Documentation is present where needed.
- [ ] Public functions/classes have docstrings
- [ ] Complex/non-obvious logic has inline comments
- [ ] Exceptions are explained where they are raised (inline, not in docstring)

**2. Accuracy** — Documentation reflects actual code.
- [ ] Parameter names in docstrings match signatures (if documented)
- [ ] Return value descriptions match implementation
- [ ] No stale documentation describing outdated behavior

**3. Substance** — Documentation adds value beyond the code.
- [ ] Explains intent ("why") not mechanics ("what")
- [ ] Documents design decisions with reasoning
- [ ] No restatement of obvious code operations
- [ ] Clarifies non-obvious assumptions or edge cases

**4. Economy** — Documentation is free of redundancy.
- [ ] No tautological descriptions (e.g., `@param name The name`)
- [ ] Skip `@param` for self-explanatory parameters (rely on type hints)
- [ ] Simple functions: single-line docstrings; complex: multi-line
- [ ] No section headers (Args/Returns) for trivial functions

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]

---

(The appendix should also be included in the report for reference)

**Python docstring (Sphinx Style):**

# Single-line: One space before and after triple quotes
""" Brief description of what this does. """

# Multi-line
""" 
Brief description.
:param x: X coordinate.
:return: Dictionary with metrics.
"""

**C++ docstring (Doxygen Style):**

/**
 * @brief Brief description of function purpose
 * @param param1 Description of parameter
 * @param param2 Description of parameter
 * @return Description of return value
 * @throws ExceptionType When this occurs
 */
```

### Wheel Reinvention Reviewer

Detect redundant code that duplicates existing functionality from third-party libraries or workspace utilities. *Tradeoff: Don't let "don't reinvent the wheel" become "add a dependency for every line of code". Balance reuse with simplicity.*

```
**1. Library Duplication** — Check if code replicates third-party library functionality.
- [ ] No manual implementations of common utilities (deep clone, debounce, throttle, etc.)
- [ ] No custom regex patterns for standard formats (email, URL, date) when validation libraries exist
- [ ] No hand-rolled data structures when language/library equivalents suffice
- [ ] No reimplementation of standard algorithms (sort, search, hash) without performance justification

**2. Workspace Duplication** — Check if code duplicates existing internal utilities.
- [ ] No duplicate helper functions across different modules
- [ ] No redundant wrapper functions that just forward to existing utilities
- [ ] Consistent use of shared utility modules (constants, formatters, validators)
- [ ] No parallel implementations of the same feature in different files

**3. Dependency Cost-Benefit** — Evaluate if adding a dependency is worth it.
- [ ] No heavy libraries added for trivial functionality (< 20 lines)
- [ ] No dependencies for one-liners that are clear when written inline
- [ ] Consider dependency tree size, not just the direct package
- [ ] Prefer standard library / built-in solutions when adequate

**4. Integration Opportunities** — Identify code that should use existing abstractions.
- [ ] Code that mirrors existing class/module interfaces
- [ ] Repeated patterns that could use shared base classes
- [ ] Configuration/logic that duplicates existing defaults

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Bug Finder Reviewer

Scan code for real defects only. Flag runtime bugs, security issues, resource leaks, and race conditions. Skip noise.

```
**Noise to Skip** — Do NOT flag these:
- [ ] Type annotation misleading caller (`arg: str = None`, return may be `None` but not `Optional`)
- [ ] Math/library natural semantics (empty mean=nan, shape mismatch ValueError, singular LinAlgError)
- [ ] Caller-known preconditions / runtime errors as contracts (API contract, upstream logic, or dict key / attribute access where Python raises naturally — do NOT demand defensive checks unless input is untrusted)
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
**1. README Essentials** — Commands > prose.
- [ ] One-line project description
- [ ] Install/setup commands copy-paste ready
- [ ] Minimal working example (hello world)
- [ ] Quickstart for common use cases

**2. API Documentation** — Reference for users.
- [ ] Public API surface documented
- [ ] Configuration options explained with examples
- [ ] Error messages and troubleshooting guide
- [ ] Changelog or version migration notes

**3. Design/Architecture Docs** — For contributors.
- [ ] High-level architecture overview (diagrams if complex)
- [ ] Development setup instructions
- [ ] Contribution guidelines (CONTRIBUTING.md)
- [ ] Code of conduct and license info

**4. Additional Guides** — Tutorials and how-tos.
- [ ] Deployment/production guides if applicable
- [ ] FAQs for common issues
- [ ] Performance considerations
- [ ] Security best practices

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Clarity Reviewer

Remove AI flavor and improve directness in writing. *Tradeoff: Directness can sacrifice nuance. Preserve important qualifications.*

```
**1. Cut the Fluff** — Remove filler that adds no information.
- [ ] No AI-flavored phrases (specifically, in summary, etc.)
- [ ] No vague modifiers without substance (very, obviously)
- [ ] No redundant statements

**2. Direct Statements** — Say what you mean without hedging.
- [ ] Circuitous expressions replaced with direct statements
- [ ] Unnecessary qualifiers removed
- [ ] Conclusions stated plainly

**3. Flow Over Fragmentation** — Write paragraphs, not telegrams.
- [ ] One-sentence paragraphs combined
- [ ] Logical paragraph structure
- [ ] Coherent flow maintained

**4. Show Don't Declare** — Demonstrate importance, don't label it.
- [ ] No "importantly" or "it is worth noting that"
- [ ] Content shows importance, not labels
- [ ] Facts presented without telling reader what to think

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

### Academic Style Reviewer

Follow academic writing conventions and domain standards. *Tradeoff: Rigid conventions can reduce readability. Balance formality with clarity.*

```
**1. Consistent Conventions** — Follow the domain's established patterns.
- [ ] Abbreviations defined on first use
- [ ] Domain-standard citations (Fig./Tab.)
- [ ] Field-specific terminology followed
- [ ] Formatting consistent

**2. Formal Presentation** — Write for the academic context.
- [ ] No bold in running prose
- [ ] Consistent section hierarchy
- [ ] Tables/figures properly formatted
- [ ] Appropriate formality level

**3. Precise References** — Cite sources clearly and consistently.
- [ ] Claims backed by citations
- [ ] Consistent citation format
- [ ] Clear attribution
- [ ] Original contribution distinguished

**4. Structured Communication** — Organize for academic readers.
- [ ] Clear section hierarchy
- [ ] Abstract present and accurate
- [ ] Methods reproducible
- [ ] Results distinct from interpretation

Report:
| Location | Issue | Severity |
|----------|-------|----------|

Score: [1-10]/10
Summary: [Brief overview of key observations]
```

---

## Appendix

### Update Log

> **Versioning Policy**: Use minor versions (v1.1, v1.2...) for incremental updates. Only bump major version (v2.0) when explicitly requested by the author.

- **v1.5**: Refined Architecture Reviewer (Local Reasoning) check 2 — Expanded "no fragmented knowledge" to explicitly cover overly granular file splitting alongside module fragmentation
- **v1.4**: Added "Appropriate Verbosity" check to Code Comments Reviewer — Detects excessive, redundant, and overly detailed documentation that adds no value over self-documenting code
- **v1.3**: Added Wheel Reinvention Reviewer to Code Review group — Detects code that duplicates third-party library functionality or workspace utilities, and flags unnecessary heavy dependencies for trivial functionality
- **v1.2**: Split Documentation Reviewer into Code Comments Reviewer (Code Group) and Documentation Reviewer (Writing Group) — Code Comments focuses on inline code docs and docstrings; Documentation covers project-level docs (README, API docs, guides)
- **v1.1**: Added Documentation Reviewer agent to Code Review group — Evaluates code documentation quality including inline comments, function docs, and API documentation completeness
- **v1.0**: Initial release — Multi-agent review system with 4 specialized reviewers (AI Artifacts, Architecture, Clarity, Academic Style), inline taglines, merged desc/tradeoff format
