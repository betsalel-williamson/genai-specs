# Swift Code Organization

## Problem

Well-organized code is easier to navigate, understand, and maintain.

## Solution

### MARK Comments

Use MARK comments to organize code sections:

```swift
class MyClass {
    // MARK: - Properties

    private let service: Service
    private var items: [Item] = []

    // MARK: - Initialization

    init(service: Service) {
        self.service = service
    }

    // MARK: - Public Methods

    func publicMethod() {
        // ...
    }

    // MARK: - Private Methods

    private func privateMethod() {
        // ...
    }
}
```

### Extensions for Protocol Conformance

Separate protocol conformance into extensions:

```swift
// Main class definition
class CubeState {
    let faces: [Face: [Color]]

    init(faces: [Face: [Color]]) {
        self.faces = faces
    }
}

// Protocol conformance in extension
extension CubeState: Equatable {
    static func == (lhs: CubeState, rhs: CubeState) -> Bool {
        lhs.faces == rhs.faces
    }
}

extension CubeState: CustomStringConvertible {
    var description: String {
        "CubeState with \(faces.count) faces"
    }
}
```

### File Organization

#### Single Type Per File

Prefer one main type per file:

```
Models/
├── CubeState.swift
├── Move.swift
├── Algorithm.swift
└── Face.swift
```

#### Group Related Types

Small, tightly related types can share a file:

```swift
// Color.swift
enum Color: String, CaseIterable {
    case white, yellow, red, orange, green, blue
}

extension Color {
    var displayName: String {
        rawValue.capitalized
    }
}
```

### Property Organization

Order properties consistently:

```swift
class ViewModel {
    // MARK: - Properties

    // 1. Static properties
    static let defaultTimeout = 30.0

    // 2. Public properties
    var items: [Item] = []

    // 3. Internal properties
    let service: Service

    // 4. Private properties
    private var cache: [String: Data] = [:]

    // 5. Computed properties
    var count: Int {
        items.count
    }
}
```

### Method Organization

Order methods by visibility and purpose:

```swift
class MyClass {
    // MARK: - Initialization

    init() { }

    // MARK: - Public Interface

    public func publicMethod() { }

    // MARK: - Internal Methods

    func internalMethod() { }

    // MARK: - Private Helpers

    private func helperMethod() { }
}
```

### Group Related Functionality

Use nested types for related functionality:

```swift
class CubeValidator {
    enum ValidationError: Error {
        case invalidColorCount
        case invalidEdge
        case invalidCorner
    }

    struct ValidationResult {
        let isValid: Bool
        let errors: [ValidationError]
    }

    func validate(_ cube: CubeState) -> ValidationResult {
        // Validation logic
    }
}
```

## Impact

Consistent organization makes code easier to navigate and understand.

## Takeaways

- Use MARK comments to divide code into logical sections
- Put protocol conformance in extensions
- Prefer one main type per file
- Order properties and methods consistently
- Use nested types for related functionality
- Group related files in directories by feature or layer

