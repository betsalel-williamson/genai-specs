# `local` Declarations in Functional Constructs

- **Error**: ``Unexpected token `local`.``
- **Cause**: Attempting to use `local` declarations directly within lambda expressions passed to functional methods like `map` or `flatMap`.
- **Resolution**: `local` declarations are statements, not expressions, and cannot be used directly within these contexts. Instead, ensure the lambda body is a single expression that returns the desired value. If intermediate variables are needed, they must be defined outside the lambda or the logic refactored to avoid them within the lambda.
