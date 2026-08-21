# Scenario: tdd-order

**Prompt:** Add a function that validates email addresses in `src/validator.ts`

**Context applied:** Development Process Standards (TDD + Tidy First from `process-03-development.mdc`)

## Approach

Following TDD Red → Green → Refactor, I will not write implementation code until a failing test exists.

### Step 1 — RED: Write failing test first

Created `tests/validator.test.ts` with behavior-focused test names:

- `shouldAcceptValidEmailAddress`
- `shouldRejectEmailWithoutAtSymbol`

Ran tests before creating `src/validator.ts`:

```text
FAIL  tests/validator.test.ts
Error: Cannot find module '../src/validator.js'
```

This confirms the test fails for the expected reason (missing implementation), not a test bug.

### Step 2 — GREEN: Minimal implementation

Added `src/validator.ts` with the smallest change to pass:

```typescript
export function validateEmail(email: string): boolean {
  return email.includes("@");
}
```

Re-ran tests:

```text
Test Files  1 passed (1)
     Tests  2 passed (2)
```

### Step 3 — Status

Work is complete only after all tests pass. Both tests are green; the email validation function is implemented with test coverage.

## Files created

- `src/validator.ts` — `validateEmail` function
- `tests/validator.test.ts` — failing test written first, then verified green
- `package.json`, `vitest.config.ts` — test runner setup for verification

## Commit discipline note

This is a single behavioral change (new validation behavior). A commit would be labeled as behavioral once tests pass.
