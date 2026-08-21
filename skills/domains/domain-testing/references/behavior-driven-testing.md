# Behavior-Driven Testing

Focus on testing behavior and outcomes rather than implementation details.

## Core Principles

### Test Behavior, Not Implementation

- Tests should verify expected behavior, treating implementation as a black box
- Test through the public API exclusively - internals should be invisible to tests
- No 1:1 mapping between test files and implementation files
- Tests that examine internal implementation details are wasteful and should be avoided

### Business Behavior Focus

- **Coverage targets**: 100% coverage should be expected at all times, but tests must ALWAYS be based on business behavior, not implementation details
- Tests must document expected business behavior
- Focus on user-facing outcomes and system behavior
- Avoid testing internal methods or private functions directly

### Test Organization

- Group tests by feature or business capability, not by code structure
- Use descriptive test names that describe behavior (for example, "shouldCalculateDiscountForPremiumCustomers")
- Organize tests to tell a story about the system's behavior

## Testing Tools and Frameworks

### Recommended Tools

- **Jest** or **Vitest** for testing frameworks
- **React Testing Library** for React components (when applicable)
- **MSW (Mock Service Worker)** for API mocking when needed
- Follow the same code quality standards in test code as production code

### Mock Strategy

- Only mock dependencies when tests are expensive (slow I/O, network calls, complex setup)
- For cheap tests (simple functions, local file system interactions), prefer real implementations
- Use real schemas and types in tests - never redefine them in test files
- Mock at the boundary of your system, not internal components
