# Strict Mode is Mandatory

**Rationale:** Strict mode catches entire classes of common errors at compile time.

**Rule:** All `tsconfig.json` files must enable `"strict": true` and its constituent flags (`noImplicitAny`, `strictNullChecks`, etc.).
