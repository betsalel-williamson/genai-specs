# Reading YAML Files

- **Rule**: When reading YAML files, use `pkl:yaml` and explicitly parse the file contents.
- **Example**:

  ```pkl
  import "pkl:yaml" as yaml

  fileContents = read("file:../../api/openapi.yaml").text
  local openApiSpec = new yaml.Parser {}.parse(fileContents)
  ```
