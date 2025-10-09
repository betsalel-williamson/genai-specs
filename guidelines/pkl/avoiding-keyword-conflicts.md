# Avoiding Keyword Conflicts in Target Languages

- **Problem**: When defining Pkl schemas (ASTs) that will be used to generate code for multiple platforms (for example, Swift, TypeScript, Java), using property names that are reserved keywords in those target languages can cause compilation errors or require complex, language-specific escaping in the generators.

- **Rule**: Avoid using common programming language keywords as property names in your Pkl modules. Prefer descriptive, non-keyword alternatives.

- **Examples of keywords to avoid**: `class`, `id`, `type`, `for`, `in`, `if`, `else`, `public`, `private`, `static`, `function`, `var`, `let`, `const`, etc.

- **Recommendation**: Use more descriptive names or add a prefix/suffix to avoid collisions.

- **Incorrect (High Risk)**:

  ```pkl
  class UIComponent {
    id: String // 'id' is a common keyword/property name.
    class: String // 'class' is a keyword in many languages.
    type: String // 'type' is a keyword in many languages.
  }
  ```

- **Correct (Low Risk)**:

  ```pkl
  class UIComponent {
    componentId: String
    cssClass: String
    componentType: String
  }
  ```

- **Rationale**: By choosing safer names in the Pkl source of truth, we make the code generators for each target platform simpler and more robust. They won't need to contain complex logic to handle keyword escaping for every language they support.
