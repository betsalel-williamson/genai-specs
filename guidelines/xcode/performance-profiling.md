# Performance Profiling with Instruments

## Problem

Performance issues need measurement before optimization to avoid premature optimization.

## Solution

### Launch Instruments

```bash
# From Xcode
⌘I (Product → Profile)

# From command line
open /Applications/Xcode.app/Contents/Applications/Instruments.app
```

### Key Instruments

#### Time Profiler

Identify CPU-intensive code:

1. Run app in Instruments with Time Profiler
2. Perform actions that feel slow
3. Stop recording
4. Examine call tree
5. Focus on "heaviest" stack traces
6. Look for unexpected hot paths

**Common issues to look for:**
- Expensive operations on main thread
- Unnecessary repeated calculations
- Inefficient algorithms

#### Allocations

Track memory usage:

1. Run with Allocations instrument
2. Look for growing memory usage
3. Take memory snapshots at different points
4. Compare snapshots to find leaks
5. Filter by allocation type

**Key metrics:**
- Overall memory usage
- Memory growth over time
- Large allocations
- Allocation patterns

#### Leaks

Find memory leaks:

1. Run with Leaks instrument
2. Leaks are automatically detected
3. Click leak to see allocation stack trace
4. Common causes: retain cycles, closures capturing self

**Common patterns:**
```swift
// BAD: Retain cycle
class ViewModel {
    var completion: (() -> Void)?

    func setup() {
        completion = {
            self.doSomething()  // Captures self strongly
        }
    }
}

// GOOD: Weak self
class ViewModel {
    var completion: (() -> Void)?

    func setup() {
        completion = { [weak self] in
            self?.doSomething()
        }
    }
}
```

#### Core Animation

Measure graphics performance:

1. Run with Core Animation instrument
2. Look at FPS (frames per second)
3. Target 60 FPS for smooth animations
4. Check for dropped frames

### Performance Optimization Guidelines

1. **Profile first**: Don't optimize without measuring
2. **Focus on hot paths**: Optimize where it matters most
3. **Test on real devices**: Simulators don't reflect real performance
4. **Monitor battery impact**: Use Energy Log instrument

### Common Optimization Patterns

```swift
// Lazy initialization
class MyViewModel {
    private lazy var expensiveResource = createExpensiveResource()
}

// Caching
actor CacheService {
    private var cache: [CubeState: Algorithm] = [:]

    func getSolution(for state: CubeState) async -> Algorithm? {
        if let cached = cache[state] {
            return cached
        }
        let solution = await computeSolution(state)
        cache[state] = solution
        return solution
    }
}

// Background processing
@MainActor
class ViewModel: ObservableObject {
    func processData() async {
        // Process off main thread
        let result = await heavyComputation()
        // Update UI on main thread
        self.result = result
    }
}
```

## Impact

Profiling identifies real performance bottlenecks and guides effective optimization.

## Takeaways

- Always profile before optimizing
- Use Time Profiler to find CPU bottlenecks
- Use Allocations to track memory usage
- Use Leaks to find memory leaks
- Use Core Animation for graphics performance
- Test on minimum supported device
- Focus optimization efforts on measured hot paths
- Avoid premature optimization

