# Collection member & element separators

- **Error**: `Unexpected token ','. Expected '}'`.

- **Cause**: Using a comma (`,`) to separate members or elements within a `new Mapping {}` or `new Listing {}` block.

- **Resolution**: Separate members/elements within these blocks with whitespace (idiomatically, a newline) or a semicolon (`;`). Reserve commas for things like function arguments.

- **Rule**: Don't use commas inside `new Listing {}`, `new Mapping {}`, or `new {}` blocks to separate items.

- **Incorrect Listing**:

  ```pkl
  myList = new Listing { "a", "b" } // Invalid comma
  ```

- **Correct Listing**:

  ```pkl
  myList = new Listing {
    "a"
    "b"
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
