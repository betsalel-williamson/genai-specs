---
name: create-skill
description: Use when creating, structuring, or authoring a new Agent Skill, SKILL.md frontmatter, skill folder layout, or converting rules into skills for Cursor.
---

# Create Skill

Guide for authoring Agent Skills compatible with [agentskills.io](https://agentskills.io/specification) and Cursor.

## Directory layout

```text
skill-name/
  SKILL.md          # required
  references/       # optional deep docs
  assets/           # optional templates
  scripts/          # optional deterministic tools
```

Store project skills under `skills/` following existing tier folders: `_meta/`, `sdlc/`, `engineering/`, `domains/`, `verification/`.

## SKILL.md frontmatter

```yaml
---
name: skill-name
description: Use when [specific triggers and symptoms only — no workflow summary]
paths: "**/*.ext"   # optional Cursor scope
---
```

- `name`: lowercase letters, numbers, hyphens; matches folder name
- `description`: third person, starts with "Use when"; triggers only
- `paths`: optional glob scope for domain skills

## Workflow

1. Decide skill type: technique, pattern, reference, or discipline
2. Draft minimal `SKILL.md` under 500 lines; shard overflow to `references/`
3. Add templates to `assets/` when output shape must be fixed
4. For discipline skills, run baseline scenarios before deploying (see `skill-authoring`)
5. Commit under `skills/` and verify discovery in Cursor Settings → Rules

## Checklist

- [ ] Description is triggers-only (no workflow summary in YAML)
- [ ] Body uses imperative instructions and clear output contracts
- [ ] Heavy content lives in `references/`
- [ ] Cross-references use skill names, not `@` file paths
- [ ] Eval scenarios exist for discipline or template skills

See also: `skill-authoring` hub for eval loops and bulletproofing.
