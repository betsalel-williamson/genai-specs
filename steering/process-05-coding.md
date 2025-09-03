---
inclusion: always
---

# General Coding Guidelines

Universal coding practices that apply across all languages and technologies.

## Code Organization Principles

### Function Design

- Keep functions small and focused on a single responsibility
- Use descriptive names that clearly express intent
- Prefer pure functions without side effects when possible
- Make dependencies explicit through parameters

### Data Patterns

- Prefer immutable data structures
- Use factory functions for creating test data and complex objects
- Accept optional overrides for flexibility: `(overrides?: Partial<T>) => T`
- Build incrementally - extract nested object factories as needed

### Naming Conventions

- Use descriptive names over abbreviated ones
- Express intent clearly through naming and structure
- Avoid generic names like **data**, **info**, **manager**
- Use domain-specific terminology consistently

## Test Data Factory Pattern

Use factory functions with optional overrides for consistent test data:

```typescript
// Example pattern (adapt to your language)
const createMockUser = (overrides?: Partial<User>): User => {
  return {
    id: 'user-123',
    name: 'Test User',
    email: 'test@example.com',
    createdAt: new Date(),
    ...overrides,
  };
};

// Usage
const user = createMockUser({ name: 'Custom Name' });
```

**Key principles:**

- Always return complete objects with sensible defaults
- Accept optional overrides for customization
- Compose factories for complex nested objects
- Use consistent naming patterns across factories

## Error Handling

### Explicit Error Management

- Handle errors explicitly rather than letting them bubble up silently
- Provide meaningful error messages that help with debugging
- Use appropriate error types for different failure modes
- Consider error boundaries and graceful degradation

### Validation Patterns

- Validate inputs at system boundaries
- Use schema validation for external data
- Fail fast with clear error messages
- Separate validation logic from business logic

## Code Quality Standards

### Duplication Management

- Remove duplication of knowledge, not just code
- Allow similar code when representing different business concepts
- Extract shared behavior only when it represents the same domain concept
- Prefer composition over inheritance

### Dependency Management

- Make dependencies explicit
- Minimize coupling between components
- Use dependency injection for testability
- Avoid circular dependencies
