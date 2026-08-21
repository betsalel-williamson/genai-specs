# Use Options Objects for Function Parameters

**Rationale:** Options objects make function calls self-documenting, improve readability, and make adding new optional parameters a non-breaking change.

**Rule:** Functions with more than two parameters, or with any optional parameters, MUST accept a single options object.
**Rule:** Use destructuring with default values at the beginning of the function to handle options.

**Example (avoid):** `function(id: string, count: number, isActive?: boolean)`
**Example (prefer):** `function({ id, count, isActive = false }: Options)`
