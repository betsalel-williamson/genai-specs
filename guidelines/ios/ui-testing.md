# SwiftUI UI Testing with XCUITest

## Problem

UI testing requires understanding XCUITest patterns for interacting with UI elements and verifying behavior.

## Solution

### Basic UI Test Structure

```swift
import XCTest

final class ScanningUITests: XCTestCase {
    var app: XCUIApplication!

    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        app = XCUIApplication()
        app.launch()
    }

    func testStartScanningFlow() {
        // Navigate to scanning
        app.buttons["Scan Cube"].tap()

        // Verify camera permission alert appears
        let alert = app.alerts["Allow Camera Access"]
        XCTAssertTrue(alert.waitForExistence(timeout: 2))

        // Grant permission
        alert.buttons["Allow"].tap()

        // Verify camera view appears
        let cameraView = app.otherElements["CameraView"]
        XCTAssertTrue(cameraView.waitForExistence(timeout: 2))
    }
}
```

### Querying Elements

```swift
// By identifier
app.buttons["submitButton"]
app.textFields["emailField"]

// By label
app.buttons["Submit"]
app.staticTexts["Welcome"]

// By type
app.buttons.firstMatch
app.textFields.element(boundBy: 0)

// Predicates
let button = app.buttons.matching(
    NSPredicate(format: "label CONTAINS[c] 'submit'")
).firstMatch
```

### Interacting with Elements

```swift
// Tapping
element.tap()
element.doubleTap()
element.press(forDuration: 1.0)

// Text input
textField.tap()
textField.typeText("Hello")

// Swiping
element.swipeUp()
element.swipeDown()

// Waiting
XCTAssertTrue(element.waitForExistence(timeout: 5))
```

### Assertions

```swift
// Existence
XCTAssertTrue(element.exists)
XCTAssertFalse(element.exists)

// Enabled/disabled
XCTAssertTrue(button.isEnabled)
XCTAssertFalse(button.isEnabled)

// Selected state
XCTAssertTrue(element.isSelected)

// Values
XCTAssertEqual(textField.value as? String, "Expected")
```

### Testing Navigation

```swift
func testNavigationFlow() {
    // Start at home
    XCTAssertTrue(app.navigationBars["Home"].exists)

    // Navigate to detail
    app.buttons["Details"].tap()

    // Verify detail screen
    XCTAssertTrue(app.navigationBars["Detail"].exists)

    // Navigate back
    app.navigationBars.buttons.element(boundBy: 0).tap()

    // Verify back at home
    XCTAssertTrue(app.navigationBars["Home"].exists)
}
```

### Accessibility Identifiers

Set identifiers in SwiftUI for easier testing:

```swift
// In SwiftUI view
Button("Submit") {
    // Action
}
.accessibilityIdentifier("submitButton")

TextField("Email", text: $email)
    .accessibilityIdentifier("emailField")

// In test
app.buttons["submitButton"].tap()
app.textFields["emailField"].typeText("test@example.com")
```

## Impact

Well-structured UI tests catch integration issues and ensure the app works from a user's perspective.

## Takeaways

- Use accessibility identifiers for reliable element queries
- Always use `waitForExistence(timeout:)` for elements that may load asynchronously
- Keep tests focused on user-facing behavior
- Use `continueAfterFailure = false` to fail fast
- Test critical user flows thoroughly
- Avoid testing implementation details
- Use page object pattern for complex flows

