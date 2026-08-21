# Skill Taxonomy Rationale

Why genai-specs skills are grouped into five tiers and how agents should load them.

## Design goals

1. **Progressive disclosure** — metadata always on; bodies and references load on demand
2. **Phase-first discovery** — spec-flow skills trigger from task type, not file extension alone
3. **Cursor compatibility** — skill `name` matches parent folder; optional `paths` for domains
4. **No duplication** — Superpowers skills cross-referenced for TDD, brainstorming, verification

## Tier 0: Meta (`skills/_meta/`)

Loaded when the agent needs to discover skills, shard context, or author new skills.

| Skill | Rationale |
|-------|-----------|
| `using-sdlc-skills` | Entry point; prevents loading entire library |
| `markdown-context-protocol` | Encodes L0–L3 loading rules from original genai-specs sharding |
| `skill-authoring` | Hub avoids three meta-skills competing for triggers |
| `skill-creator` | Vendored Anthropic eval and packaging tooling |
| `create-skill` | Cursor/agentskills.io structure conventions |
| `writing-skills` | Pointer to Superpowers discipline-skill methodology |

## Tier 1: Spec-flow (`skills/sdlc/`)

Maps 1:1 from `standards-*.mdc`. Triggered by requirements/design/task work, not by source file type.

Templates live in `assets/` so output shape is stable without bloating `SKILL.md`.

## Tier 2: Engineering (`skills/engineering/`)

Maps from `process-*.mdc`. These apply across stacks during implementation.

`engineering-core-principles` shards evidence-based content to `references/` to stay under 500 lines.

## Tier 3: Domains (`skills/domains/domain-*/`)

Maps from `guidelines-*.mdc` + `guidelines/` shards. Folder names use `domain-{stack}` prefix so skill names match Cursor folder rules while remaining searchable.

`paths` frontmatter replaces legacy `.mdc` globs.

## Tier 4: Verification (`skills/verification/`)

Behavioral compliance and migration tooling. Subagent prompts in `agents/` delegate clean-room evals without loading full rule corpora.

## What was not migrated to always-on rules

Legacy `alwaysApply: true` process rules become on-demand skills. Agents load them when the task matches the description, matching the README’s “structured prompts over strict rules” direction.

## Cursor discovery

After clone, run:

```bash
./scripts/setup-cursor-skills.sh
```

This creates `.cursor/skills` → `skills/`. Cursor walks the tree recursively; category folders group skills without changing names.
