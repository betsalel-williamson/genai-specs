# Schema-First Development

**Rationale:** Defining schemas (for example, with Zod) provides a single source of truth for both runtime validation and static types, eliminating drift between them.

**Rule:** For any data structure that crosses a boundary (API, database, user input), define a schema first.
**Rule:** Derive TypeScript types from the schema using `z.infer<typeof MySchema>`.
**Rule:** Use the schema to parse and validate data at runtime boundaries.
**Rule (critical):** Tests MUST import and use the real, authoritative schemas from the application, not redefine or mock them. This ensures tests are always in sync with the actual data contracts.
