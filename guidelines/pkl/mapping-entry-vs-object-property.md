# Mapping Entry vs. Object Property

- **Error**: `Object of type 'Mapping' cannot have a property (other than 'default').`

- **Cause**: This error occurs when you try to assign a generic Pkl object (created with `new { ... }`) as a value within a `Mapping` entry, instead of providing a value that matches the mapping's declared type. A `Mapping` can only contain _entries_ (for example, `["key"] = value`), not _properties_ (for example, `key = value`). The `new { prop = "value" }` syntax creates a standard object with a property, which isn't a `Mapping` instance itself.

- **Incorrect Example**:

  ```pkl
  // This is a mapping whose values must also be mappings.
  properties: Mapping<String, Mapping<String, String>> {
    // INCORRECT: `new { ... }` creates a generic object, not a Mapping instance.
    // This attempts to assign a property to the outer mapping.
    ["source"] = new { type = "string" }
  }
  ```

- **Correct Example**:

  ```pkl
  properties: Mapping<String, Mapping<String, String>> {
    // CORRECT: The value for the "source" entry is an instance of `Mapping`.
    ["source"] = new Mapping { ["type"] = "string" }
  }
  ```

- **Rule**: When providing a value for an entry in a `Mapping`, ensure the value is an instance of the type declared in the mapping's value signature. If you need a nested map-like structure, you must explicitly instantiate it with `new Mapping { ... }`.
