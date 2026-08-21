# Testing Strategies

**Rationale:** Effective testing strategies are crucial for maintaining code quality, especially when dealing with file system interactions or external dependencies.

**Guideline:**

- **Pragmatic Testing Strategies**: For tests involving file system interactions, prefer creating small, temporary physical test directories over complex in-memory mocks. This simplifies test setup, improves readability, and more accurately reflects real-world behavior, leading to more robust tests.
- **Vigilance Against `any`**: Strictly adhere to the `avoid-any-use-unknown` guideline. The accidental introduction of `any` can undermine type safety and lead to subtle bugs. Continuous vigilance is required.
