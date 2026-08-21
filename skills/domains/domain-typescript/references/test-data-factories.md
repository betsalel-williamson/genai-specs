# Test Data Factories

**Rationale:** Centralized factory functions for creating test data keep tests DRY and easy to maintain.

**Rule:** Create factory functions (for example, `createMockUser()`) for common test data objects.
**Rule:** Factories must return a complete, valid object according to its schema by default.
**Rule:** Factories must accept an optional `overrides` object (`Partial<T>`) to allow for easy customization in specific tests.
