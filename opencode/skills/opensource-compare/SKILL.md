---
name: opensource-compare
description: Compare open-source methods, libraries, frameworks, or tools to support technology selection. Use when users compare open-source options, seek alternatives, or evaluate candidate projects. Adapt dimensions to the user's needs, rate suitable dimensions out of 5, and present a table with project links and useful notes.
---

# Open-Source Comparison Guidelines

Adapt the template's middle columns to the user's use case and requested dimensions; the defaults are not a fixed checklist. Keep linked method names first and useful notes last. Omit empty sections.

```markdown
As of: YYYY-MM-DD | Use case: ... | Scope: versions/environment

| Method | GitHub Stars | Last code update | API usability (0–5) | Dependency lightness (0–5) | Notes |
| --- | ---: | --- | ---: | ---: | --- |
| [Name](official-project-url) | <count> | YYYY-MM-DD | <score>/5 | <score>/5 | <key trade-off> |

## Recommendation
<Brief, scenario-based guidance, if useful. No overall score.>

## Appendix
<Sources, commit links, scoring rationale, dependency scope, and verification limitations.>
```

- **Stars / date**: Use current official repository Stars and the latest commit changing implementation code, excluding documentation-only or other non-implementation updates. Do not substitute repository update timestamps or equate popularity with quality.
- **Scores**: Use 0–5, higher is better, with consistent criteria. Evaluate API usability on the same task; score dependency lightness by required runtime dependencies and deployment burden, including native libraries, hardware, or external services. Distinguish direct, transitive, and optional dependencies in the appendix.
- **Table / appendix**: Keep cells minimal and notes decision-relevant. Put evidence, rationale, and detailed sources in the appendix, not beside dates or scores. Never include an overall score.
- **Evidence**: Prefer official sources and align versions, environments, and scope. Mark unverifiable facts as "unknown"; do not claim hands-on testing without running it.
