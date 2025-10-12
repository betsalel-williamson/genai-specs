# Swift Type Safety

## Problem

Swift's type system prevents many runtime errors, but requires understanding how to leverage it effectively.

## Solution

### Avoid Force Unwrapping

```swift
// BAD: Force unwrapping
let value = dictionary["key"]!

// GOOD: Optional binding
if let value = dictionary["key"] {
    // Use value safely
}

// GOOD: Guard statement
guard let value = dictionary["key"] else {
    return
}
```

### Use Enums for Fixed Sets of Values

```swift
// BAD: String constants
let direction = "up"

// GOOD: Enum
enum Direction {
    case up, down, left, right
}
let direction: Direction = .up
```

### Leverage Optionals

```swift
// Explicit optionality
var name: String? = nil

// Optional chaining
let uppercased = name?.uppercased()

// Nil coalescing
let displayName = name ?? "Anonymous"
```

### Use Value Types When Appropriate

```swift
// Struct for value semantics (copied on assignment)
struct Point {
    var x: Double
    var y: Double
}

// Class for reference semantics (shared on assignment)
class ViewModel: ObservableObject {
    @Published var state: AppState
}
```

## Impact

Proper type usage catches errors at compile time rather than runtime.

## Takeaways

- Avoid force unwrapping (`!`)
- Use enums for fixed value sets
- Embrace optionals rather than fighting them
- Choose value types (struct) vs reference types (class) intentionally
- Let the compiler help you catch errors early

