# Swift Concurrency

## Problem

Swift's modern concurrency model (async/await, actors) requires understanding proper patterns for thread-safe, performant code.

## Solution

### Main Actor for UI Updates

Always mark view models and UI-related classes with `@MainActor`:

```swift
@MainActor
class ViewModel: ObservableObject {
    @Published var state: String = ""

    func updateState() {
        state = "Updated"  // Safe on main actor
    }
}
```

### Actor for Thread-Safe State

Use actors for shared mutable state:

```swift
actor DataStore {
    private var items: [Item] = []

    func add(_ item: Item) {
        items.append(item)
    }

    func getAll() -> [Item] {
        return items
    }
}
```

### Async/Await for Asynchronous Work

Prefer async/await over completion handlers:

```swift
func loadData() async throws -> [Item] {
    let url = URL(string: "https://api.example.com/items")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode([Item].self, from: data)
}

// Usage
Task {
    do {
        let items = try await loadData()
        await MainActor.run {
            self.items = items
        }
    } catch {
        print("Error: \(error)")
    }
}
```

### Background Work with MainActor Return

```swift
@MainActor
class SolverViewModel: ObservableObject {
    @Published var solution: Algorithm?

    func solve(_ state: CubeState) async {
        // This runs off main thread
        let result = await SolverEngine.shared.solve(state)
        // Back to main thread for UI update
        self.solution = result
    }
}
```

## Impact

Proper concurrency patterns prevent data races, improve performance, and make code more maintainable.

## Takeaways

- Use `@MainActor` for all UI-related code
- Use `actor` for shared mutable state
- Prefer `async/await` over completion handlers
- Be explicit about thread context switches
- Test concurrent code thoroughly

