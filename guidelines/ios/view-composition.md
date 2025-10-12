# SwiftUI View Composition

## Problem

Complex SwiftUI views become hard to read and maintain without proper composition.

## Solution

### Extract Subviews

Break down complex views into smaller, focused components:

```swift
// BAD: Large monolithic view
struct DashboardView: View {
    var body: some View {
        VStack {
            HStack {
                Image(systemName: "person.circle")
                Text("Welcome")
                Spacer()
                Button("Settings") { }
            }
            .padding()

            ScrollView {
                ForEach(items) { item in
                    HStack {
                        VStack(alignment: .leading) {
                            Text(item.title)
                            Text(item.subtitle)
                        }
                        Spacer()
                        Text(item.value)
                    }
                }
            }
        }
    }
}

// GOOD: Composed from smaller views
struct DashboardView: View {
    var body: some View {
        VStack {
            HeaderView()
            ItemListView(items: items)
        }
    }
}

struct HeaderView: View {
    var body: some View {
        HStack {
            Image(systemName: "person.circle")
            Text("Welcome")
            Spacer()
            Button("Settings") { }
        }
        .padding()
    }
}

struct ItemListView: View {
    let items: [Item]

    var body: some View {
        ScrollView {
            ForEach(items) { item in
                ItemRow(item: item)
            }
        }
    }
}

struct ItemRow: View {
    let item: Item

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(item.title)
                Text(item.subtitle)
            }
            Spacer()
            Text(item.value)
        }
    }
}
```

### Use Computed Properties for Inline Subviews

```swift
struct MyView: View {
    var body: some View {
        VStack {
            headerView
            contentView
            footerView
        }
    }

    private var headerView: some View {
        Text("Header")
            .font(.title)
    }

    private var contentView: some View {
        ScrollView {
            // Content
        }
    }

    private var footerView: some View {
        HStack {
            Spacer()
            Text("Footer")
            Spacer()
        }
    }
}
```

### Use ViewBuilder for Flexible Composition

```swift
struct Card<Content: View>: View {
    let content: Content

    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        VStack {
            content
        }
        .padding()
        .background(Color.white)
        .cornerRadius(10)
    }
}

// Usage
Card {
    Text("Title")
    Text("Subtitle")
}
```

## Impact

Proper composition makes views easier to understand, test, and reuse.

## Takeaways

- Extract complex views into smaller, focused components
- Use computed properties for inline subviews
- Name views descriptively based on their purpose
- Keep individual views focused on a single responsibility
- Use `@ViewBuilder` for flexible composition
- Reuse common patterns across the app

