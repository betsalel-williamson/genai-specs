# MainActor Memory Corruption Crash During Deallocation

## Problem

Using `@MainActor` at the class level on SwiftUI ViewModels causes memory corruption crashes during object deallocation. The crash manifests as:

```
Exception Type: EXC_CRASH (SIGABRT)
Termination Reason: SIGNAL 6 Abort trap: 6
___BUG_IN_CLIENT_OF_LIBMALLOC_POINTER_BEING_FREED_WAS_NOT_ALLOCATED
```

The crash occurs in Swift's concurrency runtime:
- `swift::TaskLocal::StopLookupScope::~StopLookupScope()`
- `swift_task_deinitOnExecutorImpl`
- `ScannerViewModel.__deallocating_deinit`

This happens when Swift's concurrency system tries to clean up task-local storage during deallocation, but encounters memory that was never properly allocated or already freed.

## Solution

Replace class-level `@MainActor` with method-level and property-level annotations:

**❌ Problematic:**
```swift
@MainActor
final class ScannerViewModel: ObservableObject {
    @Published var isScanning: Bool = false

    func startScanning() async {
        isScanning = true
    }
}
```

**✅ Fixed:**
```swift
final class ScannerViewModel: ObservableObject {
    @MainActor @Published var isScanning: Bool = false

    @MainActor
    func startScanning() async {
        isScanning = true
    }
}
```

## Impact

This fix prevents:
- **Memory corruption crashes** during ViewModel deallocation
- **Test failures** in XCTest when ViewModels are created and destroyed rapidly
- **Production crashes** when users navigate away from screens with active ViewModels
- **Address Sanitizer errors** that mask other real issues

## Takeaways

1. **Avoid class-level `@MainActor`** on ViewModels that will be deallocated
2. **Use method-level `@MainActor`** for functions that modify UI state
3. **Use property-level `@MainActor`** for `@Published` properties that drive UI updates
4. **Test ViewModel lifecycle** with Address Sanitizer enabled to catch these issues early
5. **Swift concurrency runtime** manages task-local storage differently for class-level vs method-level actors

This pattern is especially important for SwiftUI ViewModels that perform async operations while updating UI state.
