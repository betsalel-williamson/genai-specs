# Swift Error Handling

## Problem

Proper error handling improves code reliability and provides better user feedback when things go wrong.

## Solution

### Define Domain-Specific Errors

Create meaningful error types for your domain:

```swift
enum CubeError: LocalizedError {
    case invalidState
    case unsolvable
    case invalidMove(Move)

    var errorDescription: String? {
        switch self {
        case .invalidState:
            return "The cube state is invalid"
        case .unsolvable:
            return "This cube cannot be solved"
        case .invalidMove(let move):
            return "Invalid move: \(move)"
        }
    }
}
```

### Use Result Type for Explicit Error Handling

```swift
func validateCube(_ state: CubeState) -> Result<Void, CubeError> {
    guard state.isValid() else {
        return .failure(.invalidState)
    }
    return .success(())
}

// Usage
switch validateCube(cube) {
case .success:
    print("Cube is valid")
case .failure(let error):
    print("Validation failed: \(error.localizedDescription)")
}
```

### Handle Errors in Async Context

```swift
func solveCube() async {
    do {
        let solution = try await solver.solve(cubeState)
        self.solution = solution
    } catch let error as CubeError {
        self.errorMessage = error.localizedDescription
    } catch {
        self.errorMessage = "An unexpected error occurred"
    }
}
```

### Propagate Errors with Throws

```swift
func processUserInput(_ input: String) throws -> CubeState {
    guard !input.isEmpty else {
        throw CubeError.invalidState
    }

    let state = try parseCubeState(from: input)
    try validateState(state)

    return state
}
```

## Impact

Proper error handling makes applications more robust and provides better debugging information.

## Takeaways

- Define domain-specific error types conforming to `LocalizedError`
- Use `Result<Success, Failure>` for explicit error handling
- Use `throws` for functions that can fail
- Catch specific error types before generic errors
- Provide meaningful error messages for users
- Log errors appropriately for debugging

