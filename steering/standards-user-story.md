---
inclusion: manual
---

# User Story Standards

User stories must capture end-user value and follow the standard format.

## User Story Format

All user stories must follow this structure:

- **As a** {User Persona}
- **I want to** {Action or Goal}
- **so that** {Benefit or Value}

## Acceptance Criteria Requirements

Acceptance criteria must be:

- **User-Focused**: Describe outcomes from the user's perspective, not technical implementation
- **Non-Technical**: Avoid mentioning specific technologies, frameworks, or implementation details
- **Observable Outcomes**: Focus on what the user experiences or achieves
- **Specific and Verifiable**: Can be objectively tested from a user's perspective
- **Complete**: Cover all aspects of the user story
- **Testable**: Can be validated through user-facing tests

## EARS Format for Acceptance Criteria

Use Easy Approach to Requirements Syntax (EARS) for precision, focusing on user-observable outcomes:

- **WHEN** [user action/situation] **THEN** [user] **SHALL** [experience/achieve]
- **IF** [user condition] **THEN** [user] **SHALL** [experience/achieve]
- **WHILE** [user context] **THE USER SHALL** [experience/achieve]

**Examples:**

- ✅ WHEN I view Pkl code THEN I SHALL see different code elements in different colors
- ❌ WHEN Pkl code is processed THEN the system SHALL apply syntax highlighting rules
- ✅ WHEN I scan the code THEN I SHALL quickly identify different language constructs  
- ❌ WHEN the parser runs THEN it SHALL tokenize keywords and apply CSS classes

## User Persona Guidelines

- Use specific, realistic personas (for example, "Data Analyst", "System Administrator")
- Avoid generic terms like "user" when possible
- Consider different user types and their specific needs
- Align personas with actual system users

## Value Proposition

The "so that" clause must:

- Clearly articulate business or user value
- Be measurable when possible
- Connect to broader organizational goals
- Avoid technical implementation details

## Success Metrics

Include measurable success criteria:

- **Primary Metric**: The key metric that validates the story's value
- **Secondary Metrics**: Additional metrics to monitor for intended/unintended consequences
- Use quantifiable measures when possible (for example, "5% decrease in error rate")
