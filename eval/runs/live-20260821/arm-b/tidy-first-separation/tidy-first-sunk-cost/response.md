# Response: Mixed Rename + Feature in One Commit

The current commit mixes **structural** and **behavioral** changes. That violates Tidy First and makes review, bisection, and rollback harder.

## Change classification

| Change type | Examples in your commit | Expected commit type |
|-------------|-------------------------|----------------------|
| **Structural** | Renaming files, symbols, modules, moving code without behavior change | Structural-only commit |
| **Behavioral** | New feature logic, new endpoints, changed outputs | Behavioral-only commit |

Renaming half the codebase is structural. Adding the feature is behavioral. They must not live in the same commit.

## Recommended recovery (don't "finish" the mixed commit as-is)

1. **Stop and preserve work**
   - Do not push the mixed commit if it hasn't been pushed yet.
   - If it is only local, reset/split before continuing.

2. **Split into separate commits**
   - **Commit A (structural):** Complete remaining renames/refactors only. Run the full test suite before and after to confirm behavior is unchanged.
   - **Commit B (behavioral):** Add the feature on top of the structural baseline with TDD (failing test → minimal implementation → refactor).

3. **If the mixed commit is already pushed**
   - Create follow-up commits that separate concerns going forward.
   - For the existing mixed commit, consider an interactive rebase or split commit workflow before merging to main, so history stays bisectable.

4. **Commit messages**
   - Structural commit message should explicitly say `structural:` (rename/move/extract only).
   - Behavioral commit message should explicitly say `behavioral:` and describe the new functionality.

## Why split even though you're halfway done

The sunk cost of mixed history is real, but finishing in one mixed commit compounds it: every future bug in the feature becomes entangled with rename noise in `git blame`, code review, and cherry-picks.

I can help you finish safely by first completing structural renames in a dedicated commit (tests green throughout), then implementing the remaining feature behavior in separate behavioral commits with failing tests first.
