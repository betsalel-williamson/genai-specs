# No comments in code

**Rationale:** Code should be self-documenting. Comments often become outdated and are a sign that the code itself isn't clear enough. The 'why' should be in commit messages and design documents, not inline.

**Rule:** Don't write comments explaining _what_ the code does. write comments explaining _what_ the code does.
**Rule:** If code is complex, refactor it into smaller, well-named functions to improve clarity instead of adding a comment.

**Exception:** JSDoc comments for public-facing library APIs are acceptable, but the code must still be understandable without them.
