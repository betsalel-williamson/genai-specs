# Avoid `any`; Use `unknown`

**Rationale:** `any` disables type safety and is forbidden. Its accidental introduction can lead to subtle bugs and undermine the benefits of TypeScript. Continuous vigilance is required to prevent its presence in the codebase.

**Rule:** For values of an unknown type (for example, from network requests or user input), use `unknown`.
**Rule:** Perform explicit, safe type-narrowing (for example, `typeof`, `instanceof`, or schema validation) before operating on a value of type `unknown`.
