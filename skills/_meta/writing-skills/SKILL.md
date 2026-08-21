---
name: writing-skills
description: Use when creating or bulletproofing discipline Agent Skills with pressure scenarios and TDD-for-docs, when skill-creator eval loops need rationalization tables.
---

# Writing Skills (genai-specs pointer)

Discipline-skill authoring with RED-GREEN-REFACTOR for documentation lives in Cursor Superpowers `writing-skills`.

## When this repo copy applies

Use the installed Superpowers plugin when available. This stub documents the dependency for offline or vendored workflows.

## Core loop (summary)

1. **RED** — run pressure scenarios without the skill; capture rationalizations
2. **GREEN** — write minimal SKILL.md addressing those failures
3. **REFACTOR** — add rationalization tables and red flags; re-test

## Integration

- Structure and frontmatter: `create-skill`
- Eval benchmarks and trigger tuning: `skill-creator`
- Full methodology: Superpowers `writing-skills`

See `skill-authoring` hub for the combined workflow.
