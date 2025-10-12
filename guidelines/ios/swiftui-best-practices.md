# SwiftUI Best Practices

## Problem

SwiftUI's declarative paradigm and state management require understanding proper patterns for building efficient, maintainable views.

## Solution

### State Management

#### @State for Local View State

Use `@State` for simple, view-local state:

```swift
struct MyView: View {
    @State private var isExpanded = false
    @State private var text = ""

    var body: some View {
        VStack {
            TextField("Enter text", text: $text)
            if isExpanded {
                Text(text)
            }
        }
    }
}
```

#### @StateObject for Owned View Models

Use `@StateObject` when the view owns the view model lifecycle:

```swift
struct FeatureView: View {
    @StateObject private var viewModel = FeatureViewModel()

    var body: some View {
        // View implementation
    }
}
```

#### @ObservedObject for Passed View Models

Use `@ObservedObject` when receiving a view model from a parent:

```swift
struct DetailView: View {
    @ObservedObject var viewModel: DetailViewModel

    var body: some View {
        // View implementation
    }
}
```

#### @EnvironmentObject for Shared State

Use `@EnvironmentObject` for app-wide dependencies:

```swift
@main
struct MyApp: App {
    @StateObject private var settings = AppSettings()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(settings)
        }
    }
}

struct ChildView: View {
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        Text(settings.theme)
    }
}
```

### View Composition

Extract subviews to improve readability and performance:

```swift
struct ComplexView: View {
    var body: some View {
        VStack {
            HeaderView()
            ContentView()
            FooterView()
        }
    }
}

// Extracted subviews
struct HeaderView: View {
    var body: some View {
        Text("Header")
            .font(.title)
    }
}
```

### Performance Optimization

#### Use Lazy Stacks for Long Lists

```swift
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item: item)
        }
    }
}
```

#### Minimize View Body Computation

Extract computed properties to reduce body complexity:

```swift
struct MyView: View {
    let items: [Item]

    var body: some View {
        VStack {
            headerView
            contentView
        }
    }

    private var headerView: some View {
        Text("Header")
    }

    private var contentView: some View {
        ForEach(items) { item in
            Text(item.name)
        }
    }
}
```

## Impact

Following these patterns leads to more maintainable, performant SwiftUI code with proper state management.

## Takeaways

- Use `@State` for local view state
- Use `@StateObject` when the view owns the object
- Use `@ObservedObject` when receiving objects from parents
- Use `@EnvironmentObject` for shared dependencies
- Extract subviews for better composition and performance
- Use lazy containers for long lists
- Keep view bodies simple and focused

