# Use `useEffect` Correctly and Sparingly

**Rationale:** `useEffect` is a common source of bugs and performance issues when misused.

**Rule:** Use `useEffect` **only** for synchronizing React state with an external system.
**Rule:** Do not use `useEffect` for data fetching that should be triggered by a user event. Place that logic in an event handler.
**Rule:** Do not call state setters (`setState`) inside a `useEffect` hook.
**Rule:** An effect must include a cleanup function if it establishes any subscription, timer, or connection.
