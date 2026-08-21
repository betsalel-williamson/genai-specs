---
name: using-sdlc-skills
description: Use when starting SDLC work, choosing which genai-specs skill applies, or before loading spec, engineering, domain, or verification guidance for a task.
---

# Using SDLC Skills

## Rule

Invoke relevant SDLC skills **before** acting. User instructions override skills.

## Priority

1. Phase skills (`spec-*`) for requirements, design, tasks, architecture, ADRs
2. Engineering skills for implementation discipline
3. Domain skills (path-scoped) for stack-specific work
4. Verification skills for evals and completion claims

## Discovery

- Match task phase first, not file type alone
- Use `markdown-context-protocol` for loading reference shards
- Do not `@`-force-load large files; read `references/` on demand

## Cross-references

Superpowers skills extend this library: `brainstorming`, `writing-plans`, `test-driven-development`, `verification-before-completion`, `writing-skills`.
