# Cursor Automations for SDLC Skills

Mechanical workflows suitable for Cursor Automations (see `/automate` in Cursor).

## Nightly trigger regression

**Trigger:** schedule (daily)

**Steps:**

1. Run `eval/harness/run_arm.sh B`
2. Execute trigger eval queries from `eval/trigger/*.json`
3. Post summary to team channel or open issue if pass rate drops

## Active feature plan symlink

**Trigger:** manual or branch push matching feature work

**Steps:**

```bash
FEATURE=my-feature
mkdir -p .cursor/plans
cd .cursor/plans
ln -sf "../../.work-items/${FEATURE}/task.md" "${FEATURE}-task.plan.md"
```

See `skills/sdlc/spec-task-breakdown/references/cursor-plan-bridge.md`.

## Post-migration lint

**Trigger:** pull request opened

**Steps:**

1. `npm run format` (markdownlint on `**/*.md`)
2. `vale --config .vale.ini --minAlertLevel error .`

Existing `.husky/pre-commit` covers local commits; this automation covers CI-style checks.

## Spec translation refresh

**Trigger:** manual when rules/guidelines sources change before full deprecation

**Steps:**

```bash
./scripts/translate-specs-to-skills.sh
```
