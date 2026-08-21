---
name: markdown-context-protocol
description: Use when loading large guidance, sharding context, referencing guidelines, or deciding between skill bodies versus references/ assets/ scripts/ for lean agent context.
---

# Markdown Context Protocol

Progressive disclosure for genai-specs skills. Load the minimum level required for the current step.

## Levels

| Level | Loaded when | Content |
|-------|-------------|---------|
| L0 | Always | Skill `name` + `description` metadata only |
| L1 | Skill triggered | `SKILL.md` workflow and rules |
| L2 | Step needs detail | `references/{topic}.md` |
| L3 | Deterministic work | Run `scripts/` without loading source |

## Rules

- Never `@`-force-load large trees; use skill names and relative reference links
- Domain skills use Cursor `paths` frontmatter instead of legacy `.mdc` globs
- Spec artifacts live in `.work-items/{feature}/` (`user-story.md`, `design.md`, `task.md`)
- Prefer Task/subagent exploration; load references in worker context
- Skills state **what** to do; MCP tools state **how** to reach external systems

## MCP (optional)

When an MCP skills server is configured, use `listSkills` / `getSkill` / `readSkillFile` for the same tree. See [docs/skills-migration/mcp-setup.md](../../../docs/skills-migration/mcp-setup.md).
