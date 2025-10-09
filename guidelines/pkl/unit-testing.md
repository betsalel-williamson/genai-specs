# Unit Testing in Pkl

Pkl includes a built-in test runner for verifying module logic. Tests are defined in modules that amend the standard library module `pkl:test`.

There are two primary ways to write tests: `facts` and `examples`.

## 1. Facts (Boolean Assertions)

Facts are for unit tests where you can make simple boolean assertions about expressions. A test case fails if any expression evaluates to `false`.

- **Use Case**: Testing the logic of functions, type constraints, or other fine-grained behaviors.

- **Syntax**:

  ```pkl
  amends "pkl:test"

  facts {
    ["a group of assertions for feature X"] {
      // Each of these must evaluate to true
      1 == 1
      "hello".length == 5
      myCustomFunction(10) == "expectedValue"
    }
  }
  ```

## 2. Examples (Golden File / Snapshot Testing)

Examples are for verifying the structure of a Pkl object. They work by comparing the value of an expression against a golden file (`.pkl-expected.pcf`).

- **Use Case**: This is the preferred method for testing the output of configuration modules, ASTs, and code generators. It ensures the entire structure of the output object is correct.

### Workflow

1. **Write the Test**: Create a test module that imports the module you want to test and defines an `examples` block.

   ```pkl
   // test_my_ast.pkl
   amends "pkl:test"
   import "my_ast.pkl" as MyAst

   examples {
     ["The complete AST structure"] {
       // This is the value we want to snapshot
       MyAst.theMainObject
     }
   }
   ```

2. **First Run (Generate Golden File)**: Run the test for the first time.

   ```shell
   $ pkl test test_my_ast.pkl
   ✍️ The complete AST structure
   1 examples written
   ```

   This creates a new file, `test_my_ast.pkl-expected.pcf`, containing the evaluated result. You should check this file into version control.

3. **Subsequent Runs (Verify)**: Running the test again compares the current output to the golden file.

   ```shell
   $ pkl test test_my_ast.pkl
   ✔ The complete AST structure
   100.0% tests pass
   ```

4. **Handle Failures**: If you change `my_ast.pkl` in a way that alters the output, the test will fail. Pkl creates a `test_my_ast.pkl-actual.pcf` file. Use `diff` to see the changes.

   ```shell
   diff -u test_my_ast.pkl-expected.pcf test_my_ast.pkl-actual.pcf
   ```

5. **Update Golden File**: If the change was intentional, update the golden file using the `--overwrite` flag.

   ```shell
   pkl test --overwrite test_my_ast.pkl
   ```

### CI/Automation: Handling the `--overwrite` Exit Code

**CRITICAL:** When using `pkl test --overwrite` in an automated script (like CI/CD), it's important to understand its exit code behavior.

- **The Behavior**: On the _very first run_ for a new test (when no `.pkl-expected.pcf` file exists), `pkl test --overwrite` will write the golden file and then **exit with a non-zero status code**.

- **The Intent**: This is intentional. It signals that a new baseline was created and should be reviewed and committed. A simple script that only checks for a `0` exit code will fail at this step.

- **The Solution**: The robust pattern for automation is a two-step process within a single script:
  1. **Write/Update Baseline**: Run `pkl test` with the `--overwrite` flag, but ignore a potential non-zero exit code. Then, verify that the golden file was actually created.
  2. **Verify Consistency**: Immediately run `pkl test` again _without_ the `--overwrite` flag. This second command MUST now pass with a `0` exit code, confirming the AST is consistent with its baseline.

- **Example Script Pattern**:

  ```shell
  #!/bin/bash
  set -euo pipefail

  PKL_TEST_FILE="my_test.pkl"
  EXPECTED_FILE_PATH="my_test.pkl-expected.pcf"

  echo "Step 1: Generating golden file..."
  # Use '|| true' to ignore the non-zero exit code on the initial write.
  pkl test --overwrite "$PKL_TEST_FILE" || true

  # Verify the file was actually created.
  if [ ! -f "$EXPECTED_FILE_PATH" ]; then
    echo "[FAIL] Golden file was not created."
    exit 1
  fi
  echo "Golden file is present."

  echo "Step 2: Verifying against golden file..."
  # This second run must succeed with a zero exit code.
  if pkl test "$PKL_TEST_FILE"; then
    echo "[OK] Test passed against baseline."
    exit 0
  else
    echo "[FAIL] Test failed against its own baseline."
    exit 1
  fi
  ```

This pattern ensures that test scripts are robust and correctly handle the entire lifecycle of Pkl snapshot testing.
