---
name: skill-authoring
description: Use when creating, evaluating, optimizing, or migrating Agent Skills and you need the combined authoring workflow across structure, evals, and discipline testing.
disable-model-invocation: true
---

# Skill Authoring Hub

Use the right meta-skill for each phase. Do not duplicate their full workflows here.

## Choose your entry point

| Goal | Skill | When |
|------|-------|------|
| Structure and Cursor conventions | `create-skill` | New skill folders, frontmatter, sharding |
| Evals, benchmarks, trigger tuning | `skill-creator` | Behavioral tests, description optimization |
| Discipline bulletproofing | `writing-skills` | Pressure scenarios, rationalization tables |

## Recommended sequence

1. **`create-skill`** — scaffold `SKILL.md`, references, assets
2. **`writing-skills`** — RED baseline for discipline skills; GREEN minimal body; REFACTOR loopholes
3. **`skill-creator`** — run eval sets, aggregate benchmarks, tune descriptions

## genai-specs conventions

- Skill naming: `spec-*`, `engineering-*`, `domain-*`, `agent-*`
- Templates: `skills/sdlc/*/assets/`
- Eval artifacts: `eval/sdlc/`, `eval/trigger/`, `eval/harness/`
- Conventions detail: [skill-creator/references/genai-specs-conventions.md](../skill-creator/references/genai-specs-conventions.md)

## Context loading

Follow `markdown-context-protocol` when authoring or migrating skills with large reference trees.
