# `when` for Conditional Members vs. `if` for Conditional Values

- **Rule**: Use the `when` keyword to conditionally include properties or elements in an object or listing. `when` is a statement that controls the structure of the object itself.
- **Rule**: Use an `if`/`else` expression when you need to conditionally determine the _value_ of a property. `if` is an expression that returns a value.

- **`when` Example (Structural)**:

  ```pkl
  isProduction = true

  serverConfig {
    hostname = "prod.server.com"
    when (isProduction) {
      // These properties are only included if isProduction is true
      timeout = 5.min
      logLevel = "warn"
    }
  }
  ```

- **`if` Example (Value)**:

  ```pkl
  isProduction = true

  serverConfig {
    hostname = "prod.server.com"
    // The logLevel property always exists, but its value changes.
    logLevel = if (isProduction) "warn" else "debug"
  }
  ```
