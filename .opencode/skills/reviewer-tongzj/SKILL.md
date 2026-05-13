---
name: reviewer-tongzj
description: Multi-agent review system with two agent groups - Code Review (AI Artifacts, Architecture, Code Comments, Wheel Reinvention) and Writing Review (Documentation, Clarity, Academic Style). Use whenever the user mentions code review, PR feedback, quality assessment, writing improvement, document review, or needs structured improvement targets. Triggers for phrases like "review this code", "check my PR", "improve this doc", "code quality", "improvement plan", "refactoring roadmap", "what needs improvement".
license: MIT
---

# Reviewer-TongZJ

Parallel multi-agent review system for code and writing quality assessment.

## When to Use

- Code review: "review this PR", "check code quality", "is this maintainable?"
- Writing review: "improve this doc", "remove AI flavor", "academic style check"
- Refactoring guidance: "how can I improve this code?", "architecture feedback"
- Improvement targeting: "what needs improvement", "improvement plan", "refactoring roadmap"

## Quick Usage

**Select Agent Group based on task type, then spawn ALL agents in that group:**

### For Code Review

Run all 4 agents in Code Review group:
```typescript
task(category="quick", load_skills=["reviewer-tongzj"], prompt="AI Artifacts: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], prompt="Architecture (CODE): [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Code Comments: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], prompt="Wheel Reinvention: [files]")
```

### For Writing Review

Run all 3 agents in Writing Review group:
```typescript
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Documentation: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Clarity: [document]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="Academic Style: [document]")
```

**Rule**: Only select ONE group based on the task type. Don't mix code and writing agents unless explicitly requested.

---

## Agent Roles

**Review agents = diagnostic tools that output structured improvement targets.**

### Design Principles
- **Single focus**: One quality dimension per agent
- **Structured output**: `| Location | Issue | Severity | Effort | Target |`
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
Review [files] for AI artifacts:

**1. Intent Over Action** — Comment what you mean, not what you do.
- [ ] No obvious comments stating what code does
- [ ] Intent comments explain "why" preserved
- [ ] Redundant comments removed

**2. Realistic Defense** — Handle errors that can actually happen.
- [ ] No over-defensive error handling for impossible cases
- [ ] Realistic edge case handling preserved

**3. Justified Abstractions** — Abstract only when it serves a purpose.
- [ ] No speculative "flexibility" or "configurability"
- [ ] No forwarding wrappers without purpose
- [ ] Actual duplication-reducing abstractions kept

**4. Clean Boilers** — Remove ceremony without function.
- [ ] No purposeless boilerplate
- [ ] Unused imports/variables/functions removed
- [ ] Functional code and clarity-adding code preserved

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

### Summary Statistics
- **AI Artifacts identified**: N items
- **By principle**: Intent Over Action: N | Realistic Defense: N | Justified Abstractions: N | Clean Boilers: N
- **Confidence assessment**: High/Medium/Low
```

### Architecture Reviewer (CODE)

Analyze code maintainability from cognitive, change, and operational perspectives. *Tradeoff: Perfect architecture is the enemy of working code. Optimize for the team's actual needs.*

```
Architecture Review (CODE) for [files]:

**1. Local Reasoning** — Understand a function without reading 10 other files.
- [ ] Functions/classes small and focused, with related logic colocated
- [ ] Nesting depth limited; no fragmented knowledge across many small modules
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

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

Maintainability Score: [1-10]/10
Findings Summary: [Brief overview of key observations]
```

### Code Comments Reviewer

Review inline code documentation for clarity and utility. *Tradeoff: Comments should explain intent, not restate code. When in doubt, prefer clearer code over more comments.*

```
Code Comments Review for [files]:

**1. Function/Method Signatures** — Types and docstrings.
- [ ] Type hints on params and returns
- [ ] Brief docstring (one line) explaining purpose
- [ ] :param and :return for public APIs with non-obvious semantics
- [ ] Exception types documented for functions that throw

**2. Inline Comments** — Explain intent, not mechanics.
- [ ] No comments restating obvious code (e.g., `i++ // increment i`)
- [ ] Complex logic explains the "why", not the "how"
- [ ] Design decisions noted with reasoning
- [ ] TODO/FIXME comments have issue references or context

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

Code Comments Score: [1-10]/10
Key Issues: [Brief list of blockers]
```

### Wheel Reinvention Reviewer

Detect redundant code that duplicates existing functionality from third-party libraries or workspace utilities. *Tradeoff: Don't let "don't reinvent the wheel" become "add a dependency for every line of code". Balance reuse with simplicity.*

```
Wheel Reinvention Review for [files]:

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

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

Duplication Score: [1-10]/10 (10 = perfect reuse, no reinvention)
Findings Summary: [Brief overview of key observations]

### Summary Statistics
- **Library duplication issues**: N items
- **Workspace duplication issues**: N items  
- **Unnecessary dependencies**: N items
- **Integration opportunities**: N items
- **Confidence assessment**: High/Medium/Low
```

---

## 2. Writing Review Agents

### Documentation Reviewer

Review project documentation for completeness and usability. *Tradeoff: Documentation should accelerate onboarding, not be a checklist. Prefer working examples over exhaustive descriptions.*

```
Documentation Review for [project/docs]:

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

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

Documentation Score: [1-10]/10
Coverage Summary: [What's present vs missing]
Key Gaps: [Critical documentation needs]
```

### Clarity Reviewer

Remove AI flavor and improve directness in writing. *Tradeoff: Directness can sacrifice nuance. Preserve important qualifications.*

```
Review [document] for clarity:

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

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|
```

### Academic Style Reviewer

Follow academic writing conventions and domain standards. *Tradeoff: Rigid conventions can reduce readability. Balance formality with clarity.*

```
Review [document] for academic style:

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

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|
```

---

## Appendix

### Update Log

> **Versioning Policy**: Use minor versions (v1.1, v1.2...) for incremental updates. Only bump major version (v2.0) when explicitly requested by the author.

- **v1.3**: Added Wheel Reinvention Reviewer to Code Review group — Detects code that duplicates third-party library functionality or workspace utilities, and flags unnecessary heavy dependencies for trivial functionality
- **v1.2**: Split Documentation Reviewer into Code Comments Reviewer (Code Group) and Documentation Reviewer (Writing Group) — Code Comments focuses on inline code docs and docstrings; Documentation covers project-level docs (README, API docs, guides)
- **v1.1**: Added Documentation Reviewer agent to Code Review group — Evaluates code documentation quality including inline comments, function docs, and API documentation completeness
- **v1.0**: Initial release — Multi-agent review system with 4 specialized reviewers (AI Artifacts, Architecture, Clarity, Academic Style), inline taglines, merged desc/tradeoff format
