---
inclusion: manual
---

# Task Standards

Tasks must be granular, technical work items that implement user stories through code.

## Task Requirements

Each task must:

- **Be Actionable by Code**: Focus only on writing, modifying, or testing code
- **Build Incrementally**: Each task builds on previous tasks with no orphaned code
- **Reference Requirements**: Link back to specific requirements from the requirements document
- **Be Independently Testable**: Can be verified through automated tests
- **Follow TDD**: Implement using Red-Green-Refactor cycle

## Task Structure

Tasks should include:

- **Clear Objective**: What specific code needs to be written/modified
- **Acceptance Criteria**: Verifiable technical outcomes
- **Requirements Traceability**: References to specific requirements
- **Test Strategy**: How the task will be validated

## Task Completion and Verification

- **Do NOT mark tasks as complete until ALL acceptance criteria have been fully verified.**
- Verification must involve executing the defined test strategy and confirming the expected outcomes.
- Prematurely marking tasks as complete can lead to incomplete work and hinder project progress.

## Task Sequencing

- **Start with Infrastructure**: Set up project structure and core interfaces first
- **Implement Core Logic**: Build fundamental functionality before features
- **Add Integration**: Wire components together incrementally
- **Validate Early**: Include testing tasks throughout, not just at the end

## Excluded Task Types

Do NOT include tasks for:

- User acceptance testing or user feedback gathering
- Deployment to production or staging environments
- Performance metrics gathering or analysis
- User training or documentation creation
- Business process changes
- Marketing or communication activities
- Manual testing of end-to-end flows (use automated tests instead)

## Task Granularity

- Each task should be completable in 1-4 hours
- Complex features should be broken into multiple tasks
- Each task should result in working, tested code
- Avoid tasks that require multiple days of work

**Storage Location:**
User story documents for specific features or work items should be stored within the `.work-items/{feature_name}/` directory, named `task.md`. For example, a user story document for the `pkl-highlighting` feature would be located at `.work-items/pkl-highlighting/task.md`. This structure ensures that user story documents are co-located with their related requirements and tasks, providing a clear, scalable, and traceable organization for project specifications.
