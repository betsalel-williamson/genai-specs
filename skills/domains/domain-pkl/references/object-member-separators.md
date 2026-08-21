# Object and mapping member separators

- **Error**: `Unexpected token ','. Expected '}'`.

- **Cause**: Using a comma (`,`) to separate properties in an object literal (`{}`) or entries in a mapping literal (`new Mapping {}`).

- **Resolution**: Separate members in these constructs with whitespace (idiomatically, a newline) or a semicolon (`;`). Commas aren't valid member separators in this context.

- **Rule**: Don't use commas to separate properties or entries within object or mapping literals.

- **Incorrect Object**:

  ```pkl
  myObject = {
    prop1 = "value1", // Invalid comma
    prop2 = "value2"
  }
  ```

- **Correct Object**:

  ```pkl
  myObject = {
    prop1 = "value1"
    prop2 = "value2"
  }
  ```

- **Incorrect Mapping**:

  ```pkl
  myMap = new Mapping {
    ["key1"] = "value1", // Invalid comma
    ["key2"] = "value2"
  }
  ```

- **Correct Mapping**:

  ```pkl
  myMap = new Mapping {
    ["key1"] = "value1"
    ["key2"] = "value2"
  }
  ```
