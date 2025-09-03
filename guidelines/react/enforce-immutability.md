# Enforce Immutability

**Rationale:** Direct mutation of state or props leads to bugs and unpredictable renders.

**Rule:** Never mutate state or props directly. All state updates must produce new objects or arrays, typically using spread syntax or functional state updates (`setState(c => c + 1)`).
