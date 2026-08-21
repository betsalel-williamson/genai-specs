# Test Behavior, Not Implementation

**Rationale:** Tests coupled to implementation details are brittle and slow down refactoring. Tests should verify what the user experiences, not how the component is built.

**Rule:** Use tools like React Testing Library to query for components in a way a user would (by label, text, role, etc.).
**Rule:** Do not test component internal state or instance methods. Test the rendered output and interactions.

**Example:** To test a login form, find the username and password fields by their labels, simulate typing, find the submit button by its text, simulate a click, and assert that the correct API call was made or that the UI changed as expected.
