# Local vs. module-private functions

- **Error**: `Invalid token at position. Expected a class, typealias, method, or property.`

- **Cause**: Using the `local` keyword before a `function` declaration. In Pkl, functions are private to their module by default. The `local` keyword applies to variables, not functions.

- **Resolution**: To define a function that is only accessible within the current module, simply define it without any special keywords. To expose a function to other modules, use the `hidden` keyword, but for module-private functions, no keyword is necessary.

- **Incorrect**:

  ```pkl
  local function myHelper(): String = "internal logic"
  ```

- **Correct**:

  ```pkl
  function myHelper(): String = "internal logic"
  ```

- **Rule**: Don't use the `local` keyword for function definitions. Functions are module-private by default. Functions are module-private by default.
