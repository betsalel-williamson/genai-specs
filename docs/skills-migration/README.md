# SDLC Skills Migration

Migration of genai-specs `.mdc` rules and `guidelines/` shards into Agent Skills under `skills/`.

Tracking issue: <https://github.com/betsalel-williamson/genai-specs/issues/5>

## Taxonomy

| Tier | Directory | Purpose |
|------|-----------|---------|
| Meta | `skills/_meta/` | Discovery, context protocol, skill authoring |
| Spec-flow | `skills/sdlc/` | User stories, design, tasks, architecture, ADRs |
| Engineering | `skills/engineering/` | Core principles, TDD, coding standards |
| Domain | `skills/domains/` | Path-scoped stack guidelines |
| Verification | `skills/verification/` | Agent behavioral verification |

See [overlap-matrix.md](overlap-matrix.md) and [rules-to-skills-mapping.md](rules-to-skills-mapping.md).

## A/B experiment matrix

| Arm | Configuration |
|-----|---------------|
| A | Legacy `.mdc` manual `@` inclusion |
| B | Full `skills/` library (target) |
| C | Skills + MCP `listSkills` / `getSkill` |
| D | SDLC + engineering skills only (no domains) |

Run: `eval/harness/run_arm.sh [A|B|C|D]`

Results: [ab-results/](ab-results/)

## Status

- Phase 0–5 scaffold complete
- Legacy `rules/` deprecated with pointer stubs after skills migration
- Primary gate: Arm B beats Arm A on behavioral metrics before removing legacy rules
