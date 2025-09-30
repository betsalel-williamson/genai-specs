---
inclusion: manual
---

# Spec Translation System User Story

## User Persona

**Name:** Multi-Platform Developer Maya
**Description:** Maya is a senior developer who works across multiple AI coding assistants depending on the project requirements and team preferences. She needs to maintain consistent development standards and guidelines across different platforms but finds it time-consuming to manually recreate specs for each AI assistant. Maya values efficiency and consistency in her development workflow.

## User Story

**As a** Multi-Platform Developer Maya
**I want to** have my development specs automatically translated to the appropriate format when I initialize each AI coding assistant
**so that** I can maintain consistent standards across Cursor, Kiro, Gemini, and Claude without manual duplication or separate translation steps

## Acceptance Criteria

### Primary Acceptance Criteria

**WHEN** I run `./cursor-init.sh` to set up Cursor
**THEN** I SHALL have my genai-specs automatically translated to Cursor `.cursor/rules` format

**WHEN** I run `./gemini-cli-init.sh` to set up Gemini
**THEN** I SHALL have my genai-specs automatically translated to Gemini `.gemini/settings.json` format

**WHEN** I run `./kiro-init.sh` to set up Kiro
**THEN** I SHALL have my genai-specs automatically translated to Kiro-compatible configuration files

**WHEN** I run `./claude-init.sh` to set up Claude
**THEN** I SHALL have my genai-specs automatically translated to Claude-compatible configuration files

**WHEN** the init scripts translate specs with frontmatter metadata
**THEN** I SHALL preserve the semantic meaning and scoping information in the target format

**WHEN** the init scripts translate guidelines with file references
**THEN** I SHALL maintain the reference structure appropriate for the target format

### Secondary Acceptance Criteria

**WHEN** I run any init script
**THEN** I SHALL receive clear feedback about what was translated and any warnings

**WHEN** the init scripts encounter unsupported features during translation
**THEN** I SHALL be informed about what couldn't be translated and why

**WHEN** I validate the translated specs with the target AI assistant
**THEN** I SHALL confirm they work correctly and maintain the intended functionality

## Success Metrics

**Primary Metric:** 95% of spec content successfully translates during init script execution without manual intervention

**Secondary Metrics:**

- Init script execution time under 30 seconds including translation
- Zero data loss in semantic meaning during translation
- 100% compatibility with target AI assistant configurations
- Zero additional user steps required beyond running the init script

## Value Proposition

This feature eliminates the manual overhead of maintaining specs across multiple AI coding assistants by seamlessly integrating translation into the initialization process. Users get consistent development standards across all platforms with zero additional steps beyond running the appropriate init script, reducing maintenance burden and potential inconsistencies from manual recreation.
