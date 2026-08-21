# Add Email Validation in `src/validator.ts`

## Approach

Following TDD (Red → Green → Refactor) and the `test-driven-development` sub-skill. No production code until a failing test exists.

## Step 1 — RED: Write failing tests first

Created `tests/validator.test.ts` with behavior-focused cases before any implementation:

- `shouldAcceptValidEmailAddress`
- `shouldRejectEmailWithoutAtSymbol`
- `shouldRejectEmptyEmail`

Ran tests before writing `src/validator.ts`:

```text
FAIL  tests/validator.test.ts
Error: Cannot find module '../src/validator.js'
```

The suite failed because `validateEmail` does not exist yet. This confirms the tests exercise missing functionality, not accidental passes.

## Step 2 — GREEN: Minimal implementation

Added the smallest implementation in `src/validator.ts`:

```typescript
export function validateEmail(email: string): boolean {
  if (!email) {
    return false;
  }

  return email.includes('@');
}
```

Re-ran the suite:

```text
✓ tests/validator.test.ts (3 tests)
Test Files  1 passed (1)
Tests  3 passed (3)
```

## Step 3 — REFACTOR

No refactor needed yet; behavior is minimal and tests remain green.

## Completion status

Work is marked complete only after all tests pass. The RED failure was observed before any production code was written.
