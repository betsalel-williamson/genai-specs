# Text Generation Pattern

- **Rationale**: To generate a raw text file (like source code), we use a standard pattern that works with the `pkl eval -f text` command.
- **Rule**: The Pkl module must have **only one** non-local property, and it must be named `output`.
- **Rule**: The `output` property must be of type `ModuleOutput`.
- **Rule**: All helper functions and variables used to build the output string must be declared as `local`.
- **Example**:

  ```pkl
  local name = "World"
  output = new ModuleOutput {
    value = "Hello, \(name)!"
  }
  ```
