---
inclusion: always
---

# Operational Protocols

Core operational protocols that supplement development standards.

## Communication Standards

- **Use Plain, Literal Language**
  Communicate with precision. Avoid ambiguity, jargon, and figurative language.
- **Maintain a Coaching Tone**
  Advise as one senior peer to another. The goal is collaborative improvement, not dictation.
- **Use Gender-Neutral Language**
  Always use gender-neutral language in all documentation, code comments, and communication to ensure inclusivity.
- **Quality Focus**
  All new features or components must include documentation and comprehensive, automated tests that validate their behavior.

## Code Modification Principles

- **Enforce Minimal Diff**
  When modifying existing files, produce the smallest possible logical change. Don't reformat code or make unrelated changes in the same step.
- **Surgical Changes**
  Treat user-provided source as absolute truth for structure, style, and comments. Apply only necessary changes.
- **Idiomatic Patterns**
  Follow established language and framework patterns for the codebase.

## Documentation Standards

- **Reference Project Root for Paths**
  All internal file paths referenced within documentation (for example, in architecture or design documents) must be relative to the project root. Avoid absolute file paths to ensure portability and consistency across different environments.

## Tool Usage Guidelines

- **Single Command Validation**
  All validation (building, testing, type-checking, linting) must be executable via a single command (for example, `npm run preflight`).
- **Automated Quality Gates**
  Manual steps in the development process are anti-patterns. The path to production must be fully automated.
- **Comprehensive Testing**
  Include unit tests, integration tests, and end-to-end validation as appropriate.