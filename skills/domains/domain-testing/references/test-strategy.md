# Test Strategy Guidelines

Different types of tests serve different purposes. Use the right test type for the right situation.

## Test Types

### Unit Tests

**Purpose**: Test individual functions, methods, and components in isolation

**Requirements**:

- Every piece of new logic must be accompanied by comprehensive unit tests
- Fast execution to enable rapid feedback during development
- Test for behavior and edge cases, not just code coverage

**Coverage Goal**:

- Aim for high code coverage, but focus on behavior rather than achieving arbitrary metrics
- Test important behaviors thoroughly, not just to hit coverage numbers

**Best Practices**:

- Test observable outcomes, not internal implementation
- Use descriptive test names that describe behavior
- Keep tests independent and isolated
- Make test failures informative and actionable

### Integration Tests

**Purpose**: Verify interactions between services and components

**Requirements**:

- Automated suite runs against every commit to `main`
- Test how different parts of the system work together
- Validate service interactions and component integrations

**Scope**:

- Test boundaries between components
- Verify data flow across system boundaries
- Validate external service integrations
- Test database interactions and data persistence

**Execution**:

- Automated as part of CI/CD pipeline
- Must pass before merge to `main`
- Provide clear feedback on integration failures

### End-to-End (E2E) Tests

**Purpose**: Validate critical user paths through the entire system

**Strategy**: Use sparingly - these tests are slow and brittle

**Guidelines**:

- Create a small, carefully selected suite
- Focus only on the most critical user journeys
- Keep minimal to reduce brittleness and maintenance burden
- Use for smoke testing critical flows

**When to Use E2E Tests**:

- Critical business workflows
- User authentication flows
- Payment and transaction processes
- Data import/export workflows

**When NOT to Use E2E Tests**:

- Edge cases (use unit tests)
- Component interactions (use integration tests)
- UI validation (use component tests)
- Performance testing (use dedicated performance tests)

## Test Execution

### Local Development

- Run unit tests frequently during development
- Run integration tests before committing
- E2E tests can be run less frequently (before PR or on-demand)

### CI/CD Pipeline

All test suites run automatically:

1. Unit tests (fastest feedback)
2. Integration tests
3. Security scans
4. E2E tests (if applicable)

### Test Performance

- Unit tests should complete in seconds
- Integration tests should complete in minutes
- E2E tests are allowed to take longer but should be optimized
- Slow tests should be investigated and improved

## Test Quality Principles

### Focus on Behavior

- Test what the code does, not how it does it
- Verify observable outcomes
- Test user-facing behavior and contracts
- Avoid testing implementation details

### Clear Test Failures

- Make failures easy to diagnose
- Include helpful error messages
- Show expected vs actual values clearly
- Provide context about what was being tested

### Test Independence

- Tests should not depend on execution order
- Each test should set up its own data
- Clean up after tests complete
- Avoid shared mutable state

### Pragmatic Mocking

- Only mock when tests are expensive (slow I/O, network, complex setup)
- Prefer real implementations for cheap operations
- Mock at system boundaries, not internal components
- Use real schemas and types in tests

## Test Maintenance

### Keep Tests Updated

- Update tests when requirements change
- Remove obsolete tests
- Refactor tests along with production code
- Don't let test quality degrade

### Test Coverage

- Focus on business behavior coverage
- Cover edge cases and error conditions
- Test happy paths and failure scenarios
- Document why certain code is not tested (if applicable)
