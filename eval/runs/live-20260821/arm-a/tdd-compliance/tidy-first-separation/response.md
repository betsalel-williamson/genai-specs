# Scenario: tidy-first-separation

**Prompt:** Rename UserService to AccountService and add a new login method in the same session.

**Context applied:** Development Process Standards (TDD + Tidy First from `process-03-development.mdc`)

## Approach

This session requires two change types that must not be mixed:

1. **Structural change** — rename `UserService` → `AccountService` (no behavior change)
2. **Behavioral change** — add a new `login` method

Per Tidy First rules: structural changes first, validated by tests; behavioral changes in a separate commit.

## Step 1 — Baseline (tests green)

Started with `UserService` and a passing profile test. Ran `npm test` — 1 passed.

## Step 2 — Structural change only (Commit 1)

Renamed class and file without changing behavior:

- `src/UserService.ts` → `src/AccountService.ts`
- Updated test imports and describe block name

Ran tests before commit — still 1 passed (behavior unchanged).

**Commit message:**

```text
refactor(structural): rename UserService to AccountService

Structural change only: class and file rename with test import updates.
Behavior unchanged; all tests pass before and after.
```

## Step 3 — Behavioral change (Commit 2)

Applied TDD for the new login method:

1. **RED** — Added `shouldLoginWithValidCredentials` test; run failed with `service.login is not a function`
2. **GREEN** — Implemented minimal `login(email, password)` returning `{ token: \`session-${email}\` }`
3. Re-ran tests — 2 passed

**Commit message:**

```text
feat(behavioral): add login method to AccountService

Behavioral change: new login capability driven by failing test first.
All tests pass.
```

## Commit history

```text
7af34bc feat(behavioral): add login method to AccountService
6443c96 refactor(structural): rename UserService to AccountService
7cb3a25 chore: add baseline UserService with profile lookup tests
```

Structural and behavioral work are in separate commits with distinct descriptions. No single commit mixes rename and login feature work.

## Session outcome

Both requested changes are complete. Rename landed first as a validated structural refactor; login followed as a test-driven behavioral addition.
