# `if` Expression Syntax

- **Error**: ``Unexpected token `{`. Expected `else`.``
- **Cause**: In Pkl, if the 'then' branch of an `if` expression is a block (enclosed in `{}`), it _must_ be followed by an `else` branch. Additionally, the `if` expression itself must return a value, and blocks do not implicitly return values.
- **Resolution**: Ensure that `if` expressions always have an `else` branch when the `then` branch is a block. If the `if` expression is meant to return a value, the block must contain an explicit return or be refactored into a single expression.
