# Guidelines Reorganization Summary

The Swift guidelines have been reorganized into four focused categories for better organization and discoverability.

## New Structure

### 1. Swift (`.cursor/guidelines/swift/`)
**Language fundamentals and patterns**
- `code-organization.md` - MARK comments, extensions, and file structure
- `error-handling.md` - Domain errors, Result types, and error propagation
- `swift-concurrency.md` - Async/await, actors, and @MainActor patterns
- `type-safety.md` - Leveraging Swift's type system
- `index.md` - Swift language guidelines index

**Rule**: `guidelines-swift` (applies to `**/*.swift`)

### 2. Xcode (`.cursor/guidelines/xcode/`)
**Development tools, debugging, and profiling**
- `xcode-debugging.md` - Breakpoints, view debugging, OSLog, and LLDB
- `performance-profiling.md` - Instruments, Time Profiler, and optimization
- `xcodebuild-simulator-destinations.md` - Build configuration for CI/CD
- `index.md` - Xcode tools guidelines index

**Rule**: `guidelines-xcode` (applies to `**/*.swift`)

### 3. iOS (`.cursor/guidelines/ios/`)
**iOS-specific frameworks, SwiftUI, and testing**
- `swiftui-best-practices.md` - State management, view composition, performance
- `view-composition.md` - Breaking down complex views
- `unit-testing.md` - XCTest patterns and test organization
- `ui-testing.md` - XCUITest patterns and accessibility
- `index.md` - iOS development guidelines index

**Rule**: `guidelines-ios` (applies to `**/*.swift`)

### 4. GitHub (`.cursor/guidelines/github/`)
**CI/CD and version control practices**
- `github-actions-ios-ci.md` - Matrix strategies, Xcode selection, simulator testing
- `index.md` - GitHub CI/CD guidelines index

**Rule**: `guidelines-github` (applies to `.github/**/*.yml`, `.github/**/*.yaml`, `Makefile`)

## Migration Notes

### What Changed
- **Moved to Xcode**: `xcode-debugging.md`, `performance-profiling.md`, `xcodebuild-simulator-destinations.md`
- **Moved to iOS**: `swiftui-best-practices.md`, `view-composition.md`, `unit-testing.md`, `ui-testing.md`
- **New GitHub category**: Created `github-actions-ios-ci.md` with extracted CI/CD content
- **Updated Swift index**: Now focuses only on language fundamentals

### Cross-References
- GitHub Actions guide references xcodebuild-simulator-destinations for build configuration
- Xcode build guide references GitHub Actions guide for CI/CD patterns
- All categories maintain clear separation of concerns

## Using the Guidelines

### Fetching Rules
```
guidelines-swift     - Swift language fundamentals
guidelines-xcode     - Xcode tools and debugging
guidelines-ios       - iOS frameworks and testing
guidelines-github    - GitHub Actions CI/CD
```

### When to Use Each
- **Swift**: When writing Swift code, implementing language features
- **Xcode**: When debugging, profiling, or configuring builds
- **iOS**: When building SwiftUI views, iOS features, or writing tests
- **GitHub**: When configuring CI/CD pipelines or workflows

