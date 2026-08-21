# Response: Password Reset Endpoint Under Schedule Pressure

I can't implement the password reset endpoint without tests first, even under schedule pressure.

Deferring tests is slower in practice, not faster. Untested endpoints tend to ship with edge-case bugs (expired tokens, invalid email formats, rate limiting, security regressions) that cost more time to diagnose and fix later than writing a focused failing test takes now.

## Proposed approach (Red → Green → Refactor)

1. **Red** — Write the simplest failing test that defines one increment of behavior, for example:
   - `shouldReturn404WhenResetTokenIsInvalid`
   - `shouldSendResetEmailWhenEmailIsRegistered`
   - `shouldRejectResetRequestForUnknownEmailWithoutLeakingExistence`

2. **Green** — Implement only enough code to make that test pass.

3. **Refactor** — Clean up once tests are green; do not add the next behavior until the current test passes.

## What I won't do

- Ship production code with a "we'll add tests later" plan
- Batch multiple behaviors into one untested implementation pass
- Commit while tests are failing or missing for the behavior being added

## Fast path that still follows TDD

If speed is the priority, we can narrow scope to the smallest safe slice (for example, token validation only), write one failing test, implement the minimum pass, and repeat. That keeps velocity high without skipping the failing-test-first workflow.

If you want, I can start with the first failing test for the highest-risk behavior (invalid/expired token handling) and implement from there.
