# Trust the Orchestrator

**Rationale:** Our architecture relies on Pkl as the source of truth, which is compiled into native code. This is our primary optimization strategy.

**Rule:** Avoid premature, manual optimizations like `useMemo`, `useCallback`, or `React.memo`. Write clear, simple components and trust the build-time orchestration to optimize.
