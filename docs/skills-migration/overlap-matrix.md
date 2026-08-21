# Superpowers Overlap Matrix

Do not re-implement these Superpowers skills inside genai-specs. Cross-reference instead.

| genai-specs skill | Superpowers skill | Integration |
|-------------------|-------------------|-------------|
| engineering-tdd-tidy-first | test-driven-development | REQUIRED SUB-SKILL in SKILL.md |
| agent-verification-protocol | verification-before-completion | REQUIRED SUB-SKILL in SKILL.md |
| spec-user-story | brainstorming | REQUIRED SUB-SKILL in SKILL.md |
| spec-design | brainstorming | REQUIRED SUB-SKILL in SKILL.md |
| spec-task-breakdown | writing-plans | REQUIRED SUB-SKILL in SKILL.md |
| skill-authoring | writing-skills | Hub points to Superpowers for discipline TDD |
| skill-authoring | skill-creator (vendored) | Hub points to Anthropic eval loop |
| skill-authoring | create-skill (vendored) | Hub points to structure conventions |

## Rationale

Superpowers skills are maintained upstream and loaded when installed in Cursor. genai-specs skills add SDLC templates, domain shards, and verification protocol without duplicating TDD or brainstorming workflows.

## When Superpowers is unavailable

Agents should follow the inlined discipline sections in `engineering-tdd-tidy-first` and verification sections in `agent-verification-protocol` as fallback. Full pressure-test tables remain in Superpowers `writing-skills`.
