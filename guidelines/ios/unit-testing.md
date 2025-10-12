# Swift Unit Testing with XCTest

## Problem

Writing effective unit tests in Swift requires understanding XCTest patterns and best practices.

## Solution

### Test Structure

Follow the Arrange-Act-Assert pattern:

```swift
import XCTest
@testable import ThreeXThreeCubePuzzleSolver

final class CubeStateTests: XCTestCase {
    // MARK: - Test Lifecycle

    override func setUp() {
        super.setUp()
        // Setup before each test
    }

    override func tearDown() {
        // Cleanup after each test
        super.tearDown()
    }

    // MARK: - Tests

    func testSolvedCubeIsValid() {
        // Arrange
        let cube = CubeState.solved()

        // Act
        let isValid = cube.isValid()

        // Assert
        XCTAssertTrue(isValid, "Solved cube should be valid")
    }

    func testInvalidCubeWithWrongColorCount() {
        // Arrange
        let invalidCube = CubeState(faces: createInvalidFaces())

        // Act & Assert
        XCTAssertFalse(
            invalidCube.isValid(),
            "Cube with wrong color counts should be invalid"
        )
    }

    // MARK: - Test Helpers

    private func createInvalidFaces() -> [Face: [CubeColor]] {
        // Helper method to create test data
        return [:]
    }
}
```

### Common Assertions

```swift
// Boolean assertions
XCTAssertTrue(condition)
XCTAssertFalse(condition)

// Equality assertions
XCTAssertEqual(actual, expected)
XCTAssertNotEqual(actual, expected)

// Nil assertions
XCTAssertNil(optional)
XCTAssertNotNil(optional)

// Error assertions
XCTAssertThrowsError(try someFunction())
XCTAssertNoThrow(try someFunction())

// Async assertions
await fulfillment(of: [expectation], timeout: 5.0)
```

### Testing Async Code

```swift
func testAsyncFunction() async throws {
    // Test async code directly
    let result = try await someAsyncFunction()
    XCTAssertEqual(result, expectedValue)
}

func testAsyncWithExpectation() {
    let expectation = expectation(description: "Async operation completes")

    Task {
        let result = await someAsyncOperation()
        XCTAssertEqual(result, expected)
        expectation.fulfill()
    }

    wait(for: [expectation], timeout: 5.0)
}
```

### Test Organization

Use MARK comments to organize tests:

```swift
final class FeatureTests: XCTestCase {
    // MARK: - Properties

    var sut: SystemUnderTest!

    // MARK: - Lifecycle

    override func setUp() {
        super.setUp()
        sut = SystemUnderTest()
    }

    // MARK: - Initialization Tests

    func testInitialization() { }

    // MARK: - Validation Tests

    func testValidation() { }

    // MARK: - Error Handling Tests

    func testErrorHandling() { }
}
```

## Impact

Structured tests improve maintainability and make test failures easier to diagnose.

## Takeaways

- Follow Arrange-Act-Assert pattern
- Use descriptive test method names
- Include failure messages in assertions
- Extract test helpers for reusable setup
- Use MARK comments for organization
- Test async code with async test methods or expectations
- Keep tests focused on single behaviors

