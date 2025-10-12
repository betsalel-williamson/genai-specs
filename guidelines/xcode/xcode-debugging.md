# Xcode Debugging Techniques

## Problem

Effective debugging requires understanding Xcode's debugging tools and techniques.

## Solution

### Console Logging with OSLog

Use structured logging instead of print statements:

```swift
import OSLog

extension Logger {
    static let cubeState = Logger(
        subsystem: "com.app.3x3cubesolver",
        category: "cube-state"
    )
    static let solver = Logger(
        subsystem: "com.app.3x3cubesolver",
        category: "solver"
    )
}

// Usage
Logger.cubeState.debug("Cube state initialized: \(cube.description)")
Logger.solver.info("Starting solve with algorithm: \(algorithm.name)")
Logger.solver.error("Solve failed: \(error.localizedDescription)")
```

### Breakpoints

#### Regular Breakpoints

- Click line number gutter to set breakpoint
- Right-click breakpoint for options
- Edit breakpoint to add conditions or actions

#### Exception Breakpoint

Catches all exceptions:
1. Breakpoint Navigator (`⌘8`)
2. Click `+` → Swift Error Breakpoint
3. Catches all thrown errors

#### Symbolic Breakpoints

Break on specific method calls:
1. Breakpoint Navigator (`⌘8`)
2. Click `+` → Symbolic Breakpoint
3. Enter symbol name (e.g., `UIViewController.viewDidLoad`)

#### Conditional Breakpoints

Break only when condition is true:
1. Right-click breakpoint → Edit Breakpoint
2. Add condition: `self.count > 10`

### LLDB Commands

```bash
# Print variable
(lldb) po variableName

# Print frame variables
(lldb) frame variable

# Continue execution
(lldb) continue
(lldb) c

# Step over
(lldb) next
(lldb) n

# Step into
(lldb) step
(lldb) s

# Step out
(lldb) finish

# Print expression
(lldb) expr count + 1

# Change variable value
(lldb) expr count = 42
```

### View Debugging

#### View Hierarchy Debugger

1. Run app (`⌘R`)
2. `Debug → View Debugging → Capture View Hierarchy`
3. Rotate 3D view to inspect layout
4. Select views to see constraints and properties

#### SwiftUI Inspector

In SwiftUI previews:
1. Click element while preview is running
2. Inspect state and modifiers
3. Right-click → Inspect Preview for more options

### Memory Debugging

#### Memory Graph Debugger

1. Run app
2. Click Memory Graph button in debug bar
3. Look for retain cycles (indicated by purple icons)
4. Inspect object graph

#### Instruments

Launch with `⌘I`:

- **Leaks**: Find memory leaks
- **Allocations**: Track memory usage
- **Time Profiler**: Find performance bottlenecks

### Accessibility Inspector

1. `Xcode → Open Developer Tool → Accessibility Inspector`
2. Select simulator
3. Inspect accessibility properties
4. Run audit for common issues

## Impact

Effective debugging techniques reduce time spent finding and fixing bugs.

## Takeaways

- Use `OSLog` instead of `print` for better log management
- Set exception breakpoints to catch errors early
- Use conditional breakpoints to debug specific scenarios
- Learn basic LLDB commands for interactive debugging
- Use View Hierarchy Debugger for layout issues
- Profile with Instruments to find performance issues
- Check accessibility with Accessibility Inspector

