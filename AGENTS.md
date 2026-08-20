# AGENTS.md

## Cursor Cloud specific instructions

This repository is an archived, documentation-only project (`genai-specs`): a
collection of Markdown (`.md`) and Cursor rule (`.mdc`) files. There is no
runnable application, backend, or frontend. "Development" means authoring docs
and running the prose/markdown linting toolchain over them.

### Toolchain / services

- `markdownlint-cli2` — Markdown style linting. Run with `npm run format`
  (defined in `package.json`; lints `**/*.md`).
- `vale` — prose linter (a standalone Go binary, not an npm package). Config is
  `.vale.ini`; it uses the `Google` style package plus the `GenaiSpecs`
  vocabulary in `.vale/config/vocabularies/GenaiSpecs/accept.txt`.
- `husky` — installs the `.husky/pre-commit` hook, which runs both
  `markdownlint-cli2` and `vale` before each commit.

The `prepare` npm script runs `husky && vale sync`, so `npm install` requires
the `vale` binary to already be present on `PATH` (it is installed into the
base environment). `vale sync` downloads the `Google` style package into
`.vale/Google` (git-ignored).

### Gotchas

- `.markdownlint-cli2.yaml` sets `fix: true`. Running `npm run format` (or the
  pre-commit hook) will AUTO-MODIFY Markdown files in place to fix violations.
  If you only intend to check formatting, review/revert unintended edits with
  `git checkout -- <files>` afterward.
- The repo currently has pre-existing lint findings (a couple of markdownlint
  `MD040` errors and ~168 `vale` spelling/Latin findings, mostly Swift/Xcode
  domain terms not in the vocabulary). These are pre-existing content issues,
  not environment problems — the linters running and reporting them is the
  expected, working behavior.
- `vale` runs against the whole tree with:
  `vale --no-exit --config .vale.ini --minAlertLevel error .` (as the
  pre-commit hook does). Drop `--no-exit` to get a non-zero exit on findings.
