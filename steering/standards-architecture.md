---
inclusion: manual
---

# Architecture Standards

Architecture documents provide a holistic, project-level view of the system, emphasizing business value and problem-solving at the highest level. They serve as the foundational documentation from which design decisions are derived.

## Architecture Document Structure

All architecture documents must include:

### 1. Introduction

Brief overview stating purpose, scope, and contribution to business value and problem-solving.

### 2. Business and System Context

- How the system fits into the larger business ecosystem
- Relevant business processes and value streams it supports
- Interactions with other applications and services
- Use C4 model diagrams linking technical components to business value

### 3. Architectural Drivers

- Key quality attributes (scalability, security, performance, maintainability)
- Constraints that influenced architectural decisions
- Clear articulation of how drivers relate to business objectives

### 4. Architectural Decisions

- Summary of significant architectural decisions
- References to specific ADRs
- How each decision addresses problems and contributes to system value

### 5. Logical View

- System's logical organization (modules, layers, relationships)
- Mapping to underlying technology services and components
- Focus on how logical structures support business functions

### 6. Process View

- Runtime behavior and interactions between business processes
- Data flows, event handling, and concurrency aspects
- Emphasis on value flow and potential bottlenecks

### 7. Deployment View

- System deployment including infrastructure and environments
- Mapping of application components to technology infrastructure

### 8. Data View

- Main data entities, relationships, and persistence mechanisms
- Connection of data to business objects and managing applications

### 9. Security Considerations

- Security measures linked to protection of business assets and value

### 10. Operational Considerations

- Monitoring, management, and maintenance in production
- Focus on continuous value delivery and operational bottlenecks

## Document Organization Principles

- **Abstracted Layers**: Break documentation into focused, manageable files
- **Entry Points**: High-level overview.md as system entry point
- **Specific Concerns**: Dedicated files for architectural views (data-flow.md, security-considerations.md)
- **Cross-referencing**: Robust navigation between high-level and detailed views

## Relationship to Design Documents

Architecture documents define the overarching structure and principles for the entire project. Feature-level design documents (see `standards-design.md`) must adhere to the architectural decisions and guidelines established here. Architecture documents should be referenced by design documents to ensure consistency and alignment across all levels of documentation.

## Document Creation and Storage

New architecture documents should be created by copying this `standards-architecture.md` file as a template.

**Storage Location:**
Project-level architecture documents should be stored directly within the `.kiro/architecture/` directory. For architecture specific to a major feature or subsystem, documents can be placed within `.kiro/specs/{feature_name}/architecture.md`. This structure ensures that architecture documents are organized logically, are easily discoverable, and provide a clear hierarchy for project documentation.
