---
name: reviewer-tongzj
description: Multi-agent review system with two agent groups - Code Review (karpathy-guidelines, AI Artifacts, Architecture) and Writing Review (Clarity, Academic Style). Use whenever the user mentions code review, PR feedback, quality assessment, writing improvement, document review, or needs structured improvement targets. Triggers for phrases like "review this code", "check my PR", "improve this doc", "code quality", "improvement plan", "refactoring roadmap", "what needs improvement".
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

Run all 3 agents in Code Review group:
```typescript
task(category="quick", load_skills=["reviewer-tongzj"], prompt="karpathy-guidelines: [files]")
task(category="quick", load_skills=["reviewer-tongzj"], prompt="AI Artifacts: [files]")
task(category="deep", load_skills=["reviewer-tongzj"], prompt="Architecture (CODE): [files]")
```

### For Writing Review  
Run all 2 agents in Writing Review group:
```typescript
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

### karpathy-guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

#### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

#### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

#### 3. Surgical Changes

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

#### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

**Review Prompt Template**

```
Review [files] against karpathy-guidelines:

**1. Think Before Coding**
- [ ] Assumptions stated explicitly before implementation
- [ ] Tradeoffs surfaced, not hidden
- [ ] Questions asked when unclear

**2. Simplicity First**
- [ ] No features beyond what was asked
- [ ] No abstractions for single-use code
- [ ] No speculative "flexibility" or "configurability"
- [ ] Code is minimal (would a senior engineer call it overcomplicated?)

**3. Surgical Changes**
- [ ] Only necessary lines changed
- [ ] Adjacent code not "improved" unnecessarily
- [ ] Style matches existing codebase
- [ ] Orphans from changes removed, pre-existing dead code left alone

**4. Goal-Driven Execution**
- [ ] Success criteria defined and verifiable
- [ ] Multi-step tasks have plan with verification checkpoints
- [ ] Tests pass before and after changes

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|
```

### AI Artifact Reviewer

Remove AI-generated code smells while preserving functionality.

**Tradeoff:** When in doubt, keep the code. Safety over aggressive removal.

#### 1. Intent Over Action

**Comment what you mean, not what you do.**

- Remove comments that state the obvious (`# increment i`, `# loop through items`)
- Keep comments that explain intent ("why" not "what")
- Delete redundant comments that repeat the code

#### 2. Realistic Defense

**Handle errors that can actually happen.**

- Remove try-except for impossible scenarios
- Keep error handling for realistic edge cases
- Don't wrap every line in defensive code

#### 3. Justified Abstractions

**Abstract only when it serves a purpose.**

- Remove unused "flexibility" or "configurability"
- Delete speculative wrappers that just forward calls
- Keep abstractions that actually reduce duplication

#### 4. Clean Boilers

**Remove ceremony without function.**

- Delete boilerplate not serving a purpose
- Remove unused imports, variables, functions
- Keep code that adds clarity or serves functional purpose

**Review Prompt Template**

```
Review [files] for AI artifacts:

**1. Intent Over Action**
- [ ] No obvious comments stating what code does
- [ ] Intent comments explain "why" preserved
- [ ] Redundant comments removed

**2. Realistic Defense**
- [ ] No over-defensive error handling for impossible cases
- [ ] Realistic edge case handling preserved

**3. Justified Abstractions**
- [ ] No speculative "flexibility" or "configurability"
- [ ] No forwarding wrappers without purpose
- [ ] Actual duplication-reducing abstractions kept

**4. Clean Boilers**
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

Analyze code maintainability from cognitive, change, and operational perspectives.

**Tradeoff:** Perfect architecture is the enemy of working code. Optimize for the team's actual needs.

#### 1. Local Reasoning

**Understand a function without reading 10 other files.**

- Keep functions and classes small and focused
- Limit nesting depth (max 3 levels)
- Avoid hidden side effects and implicit dependencies
- Make data flow explicit through parameters

#### 2. Stable Dependencies

**Depend on abstractions, not concretions.**

- High-level modules don't depend on low-level details
- Interfaces owned by consumers (DIP)
- No circular dependencies between modules
- Framework details isolated from business logic

#### 3. Single Point of Change

**One requirement change touches one place.**

- No duplicated code (DRY)
- Configuration externalized, not hardcoded
- Features encapsulated, not scattered
- Open for extension, closed for modification

#### 4. Observable Failures

**Bugs reveal themselves quickly with context.**

- Fail fast with clear, actionable error messages
- Error context preserved (stack traces, causes)
- Defensive boundaries at system edges, not everywhere
- Code designed for testability

**Review Prompt Template**

```
Architecture Review (CODE) for [files]:

**1. Local Reasoning**
- [ ] Functions/classes small and focused (<50 lines, <500 lines)
- [ ] Nesting depth limited (max 3 levels)
- [ ] No hidden side effects or implicit dependencies
- [ ] Data flow explicit through parameters

**2. Stable Dependencies**
- [ ] High-level modules independent of low-level details
- [ ] No circular dependencies
- [ ] Framework isolated from business logic
- [ ] Interfaces owned by consumers

**3. Single Point of Change**
- [ ] No duplicated code
- [ ] Configuration externalized
- [ ] Features encapsulated, not scattered
- [ ] Extensible without modification

**4. Observable Failures**
- [ ] Fail fast with clear messages
- [ ] Error context preserved
- [ ] Defensive boundaries at edges
- [ ] Code testable

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|

Maintainability Score: [1-10]/10
Findings Summary: [Brief overview of key observations]
```

---

## 2. Writing Review Agents

### Clarity Reviewer

Remove AI flavor and improve directness in writing.

**Tradeoff:** Directness can sacrifice nuance. Preserve important qualifications.

#### 1. Cut the Fluff

**Remove filler that adds no information.**

- Delete AI-flavored phrases: "specifically", "in summary", "interestingly"
- Remove vague modifiers without substance: "very", "extremely", "obviously"
- Cut redundant statements that say the same thing twice

#### 2. Direct Statements

**Say what you mean without hedging.**

- Replace circuitous expressions with direct statements
- Remove unnecessary qualifiers and throat-clearing
- State conclusions plainly without excessive hedging

#### 3. Flow Over Fragmentation

**Write paragraphs, not telegrams.**

- Combine one-sentence paragraphs into flowing text
- Use logical paragraph structure, not bullet lists
- Maintain coherent flow between sentences and paragraphs

#### 4. Show Don't Declare

**Demonstrate importance, don't label it.**

- Remove "importantly", "notably", "significantly" - the content should show importance
- Delete "it is worth noting that" - if it's worth noting, just note it
- Avoid telling the reader what to think; present the facts

**Review Prompt Template**

```
Review [document] for clarity:

**1. Cut the Fluff**
- [ ] No AI-flavored phrases (specifically, in summary, etc.)
- [ ] No vague modifiers without substance (very, obviously)
- [ ] No redundant statements

**2. Direct Statements**
- [ ] Circuitous expressions replaced with direct statements
- [ ] Unnecessary qualifiers removed
- [ ] Conclusions stated plainly

**3. Flow Over Fragmentation**
- [ ] One-sentence paragraphs combined
- [ ] Logical paragraph structure
- [ ] Coherent flow maintained

**4. Show Don't Declare**
- [ ] No "importantly" or "it is worth noting that"
- [ ] Content shows importance, not labels
- [ ] Facts presented without telling reader what to think

Report format:
| Location | Issue | Severity | Effort | Target |
|----------|-------|----------|--------|--------|
```

### Academic Style Reviewer

Follow academic writing conventions and domain standards.

**Tradeoff:** Rigid conventions can reduce readability. Balance formality with clarity.

#### 1. Consistent Conventions

**Follow the domain's established patterns.**

- Define abbreviations on first use, use consistently thereafter
- Use domain-standard citation formats (Fig./Tab., not Figure/Table)
- Follow field-specific terminology and notation conventions
- Maintain consistent formatting throughout

#### 2. Formal Presentation

**Write for the academic context.**

- Avoid bold text in running prose
- Use consistent section hierarchy
- Format tables, figures, and equations per domain standards
- Maintain appropriate formality level

#### 3. Precise References

**Cite sources clearly and consistently.**

- All claims backed by citations
- Consistent citation format throughout
- Clear distinction between cited work and original contribution
- Proper attribution of ideas and data

#### 4. Structured Communication

**Organize for academic readers.**

- Clear section hierarchy (IMRAD or domain-standard)
- Abstract summarizes contribution
- Methods reproducible from description
- Results distinct from interpretation

**Review Prompt Template**

```
Review [document] for academic style:

**1. Consistent Conventions**
- [ ] Abbreviations defined on first use
- [ ] Domain-standard citations (Fig./Tab.)
- [ ] Field-specific terminology followed
- [ ] Formatting consistent

**2. Formal Presentation**
- [ ] No bold in running prose
- [ ] Consistent section hierarchy
- [ ] Tables/figures properly formatted
- [ ] Appropriate formality level

**3. Precise References**
- [ ] Claims backed by citations
- [ ] Consistent citation format
- [ ] Clear attribution
- [ ] Original contribution distinguished

**4. Structured Communication**
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

- v1.0: Initial coder-tongzj skill
- v2.0: Added writing standards
- v3.0: Renamed to reviewer-tongzj, integrated Karpathy guidelines
- v4.0: Re-architected as multi-agent review system with specialized reviewers
- v5.0: Optimized table of contents - moved Karpathy principles into Code Review section
- v6.0: Removed Naming/Structure Reviewers; Restructured as agent groups (Code Review: karpathy-guidelines, AI Artifacts, Architecture; Writing Review: Clarity, Academic Style)
- v7.0: **Added improvement targeting** - Added "Improvement Target" column to all report formats for direct use as plan objectives; updated triggers and When to Use section
