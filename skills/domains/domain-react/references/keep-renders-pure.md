# Keep Renders Pure

**Rationale:** A component's render logic must be deterministic and free of side effects.

**Rule:** A component's render logic must be a pure function of its `props` and `state`.
**Rule:** Side effects (API calls, subscriptions) belong exclusively in event handlers or, when absolutely necessary for synchronization with external systems, in `useEffect`.
