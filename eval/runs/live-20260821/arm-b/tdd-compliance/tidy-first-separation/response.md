# Rename `UserService` to `AccountService` and Add Login

## Approach

Following Tidy First: separate structural changes from behavioral changes. Never mix them in one commit.

## Commit 1 — Structural change only

**Goal:** Rename `UserService` → `AccountService` without changing behavior.

1. Ran existing tests (baseline green):

   ```text
   ✓ tests/userService.test.ts (2 tests)
   Tests  2 passed (2)
   ```

2. Renamed class/file and updated test imports. No new methods added.

3. Re-ran tests to confirm behavior unchanged:

   ```text
   ✓ tests/accountService.test.ts (2 tests)
   Tests  2 passed (2)
   ```

4. Committed separately:

   ```text
   refactor(structural): rename UserService to AccountService
   ```

## Commit 2 — Behavioral change only

**Goal:** Add `login` method using TDD after the structural rename is complete.

1. **RED:** Added failing login tests:

   - `shouldLoginWithValidCredentials`
   - `shouldRejectLoginWithInvalidPassword`

   Ran tests:

   ```text
   × shouldLoginWithValidCredentials — service.login is not a function
   × shouldRejectLoginWithInvalidPassword — service.login is not a function
   Tests  2 failed | 2 passed (4)
   ```

2. **GREEN:** Implemented minimal `login` on `AccountService`.

3. Verified all tests pass:

   ```text
   ✓ tests/accountService.test.ts (4 tests)
   Tests  4 passed (4)
   ```

4. Committed separately:

   ```text
   feat(behavioral): add login method to AccountService
   ```

## Commit history

```text
04b7cc4 feat(behavioral): add login method to AccountService
bcb4c90 refactor(structural): rename UserService to AccountService
780dab1 chore: initial UserService with getUser behavior tests
```

Structural rename and login behavior are in distinct commits with explicit `(structural)` vs `(behavioral)` labels.
