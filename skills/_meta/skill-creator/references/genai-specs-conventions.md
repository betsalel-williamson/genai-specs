# genai-specs Skill Conventions

Conventions for skills migrated from the genai-specs rule library.

## Naming

| Tier | Pattern | Example |
|------|---------|---------|
| Spec-flow | `spec-{phase}` | `spec-user-story` |
| Engineering | `engineering-*` or `project-*` | `engineering-tdd-tidy-first` |
| Domain | `domain-{stack}` | `domain-typescript` |
| Verification | `agent-*` | `agent-verification-protocol` |
| Meta | descriptive kebab-case | `markdown-context-protocol` |

## Templates

| Artifact | Template path |
|----------|---------------|
| User story | `skills/sdlc/spec-user-story/assets/user-story-template.md` |
| Design | `skills/sdlc/spec-design/assets/design-template.md` |
| ADR | `skills/sdlc/spec-adr/assets/adr-template.md` |
| Task | `skills/sdlc/spec-task-breakdown/assets/task-template.md` |

## Work items

Store feature specs under `.work-items/{feature_name}/`:

- `user-story.md`
- `design.md`
- `task.md`
- optional numbered step files (`01_*.md`)

## Eval layout

```text
eval/
  sdlc/{skill-name}/scenarios.json
  trigger/{skill-name}-triggers.json
  harness/run_arm.sh
```

Arms: A=legacy `.mdc`, B=skills/, C=skills+MCP, D=skills without domains.

## Deprecation

Legacy sources remain in `rules/` and `guidelines/` as read-only references until Arm B beats Arm A on primary behavioral metrics.
