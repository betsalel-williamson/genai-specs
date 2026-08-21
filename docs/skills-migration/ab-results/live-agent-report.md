# Live Agent A/B Results (2026-08-21)

Subagent-run live scenarios from `eval/sdlc/*` comparing:

- **Arm A:** Pre-migration `.mdc` rules (`eval/runs/context/arm-a/`)
- **Arm B:** Agent Skills (`eval/runs/context/arm-b/`)

## Summary

| Arm | Assertions passed | Total | Pass rate |
|-----|-------------------|-------|-----------|
| A (legacy rules) | 15 | 15 | 100% |
| B (skills) | 15 | 15 | 100% |

**Gate:** Arm B pass rate ≥ Arm A → **PASS (tie)**

Arm B does not strictly *beat* Arm A on this run, but meets the migration gate (no regression). Both arms satisfied all behavioral assertions across 7 scenarios in 4 suites.

## By suite

| Suite | Arm A | Arm B | Delta |
|-------|-------|-------|-------|
| spec-user-story-shape | 5/5 | 5/5 | 0 |
| spec-design-structure | 2/2 | 2/2 | 0 |
| tdd-compliance | 4/4 | 4/4 | 0 |
| tidy-first-separation (pressure) | 4/4 | 4/4 | 0 |

## Scenarios exercised

1. User story non-technical AC (EARS, no tech in AC)
2. User story persona + verifiable metrics
3. Design document structure + architecture alignment
4. TDD order (test before implementation)
5. Tidy First separation (structural vs behavioral commits)
6. TDD under time pressure (refuse skip-tests)
7. Tidy First sunk cost (split mixed commit)

## Artifacts

- Raw runs: `eval/runs/live-20260821/arm-{a,b}/`
- Aggregated JSON: [live-agent-benchmark.json](live-agent-benchmark.json)

## Limitations

- Subagents played both executor and grader (self-graded). For production gate, use independent grader subagent per `skills/_meta/skill-creator/agents/grader.md`.
- Single rep per scenario; plan recommends ≥3 reps for trigger stability.
- Arm A content from git pre-migration (`77e6a5d^`); Arm B from current skills.

## Recommendation

Skills migration is **behaviorally equivalent** to legacy rules on this eval set. Proceed with PR #6; optional follow-up is independent grading and multi-rep variance analysis.
