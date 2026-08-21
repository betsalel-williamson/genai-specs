# Prefer Plain Objects and ES Modules

**Rationale:** This improves interoperability, reduces boilerplate, and enhances predictability.

**Rule:** Favor plain JavaScript objects with TypeScript types over `class` syntax for data structures.
**Rule:** Use ES module boundaries (`export`/`import`) for encapsulation, not class visibility keywords (`private`, `public`). Unexported code is private to the module.
