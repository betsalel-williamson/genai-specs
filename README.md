# Genai Spec System Documentation

This directory contains a system for AI-assisted development. The system provides guidance that automatically includes relevant standards and guidelines based on the work being performed.

This project is designed to be imported as a Git submodule into other repositories.

This system works with various AI coding assistants (e.g., Claude, Cursor, Gemini, Kiro) and provides instructions for spec-driven development.

## How the System Works

The system uses three ways to provide relevant context:

- **Always Included**: Core principles that apply to all development work
- **Conditional Inclusion**: Technology-specific guidelines loaded when working with certain file types
- **Manual Inclusion**: Specialized standards loaded when you request them using `@./rules/filename.mdc` in chat

After importing the specs and adding the process and standards prompts to your context, follow this workflow:

1. Design the system at a high-level. Create overall system architecture and make decisions.
2. Start implementing features. Open a new branch and add your design documentation and tasks.
   - If the feature is user-facing, add user-story documentation.
3. When the information is reviewed and ready, implement the feature by completing tasks using a red-green-refactor/TDD approach.
4. During this process, update documentation to ensure it matches the implementation.

![Spec Driven Workflow with AI Agent](./Spec%20Driven%20Workflow%20with%20AI%20Agent.png)

Important: LLMs tend to say "yes" to requests and add scope creep even when not prompted. Work within a value stream management framework to ensure that the features you are working on are worth the time and effort. The feature may need to be broken down into multiple smaller features.

Want to learn more? Watch my presentation given to the DORA community on September 30, 2025.

[![Watch the video](https://img.youtube.com/vi/9Goq80lgxSY/0.jpg)](https://youtu.be/9Goq80lgxSY?si=aXRjM3bF8gOsHjce&t=732)

[Link to presentation slides](https://docs.google.com/presentation/d/1nIUlmhMPMR-9znfg_rz1dVizWQVJ8rxn2JWSLxGEVMY/edit?usp=sharing)

## Directory Structure

### Core Process Files (Always Included)

- [**process-01-core.mdc**](rules/process-01-core.mdc) - Fundamental engineering principles
- [**process-02-project.mdc**](rules/process-02-project.mdc) - Project practices and spec driven workflow
- [**process-03-development.mdc**](rules/process-03-development.mdc) - TDD methodology and commit discipline
- [**process-04-operational.mdc**](rules/process-04-operational.mdc) - Communication and quality standards
- [**process-05-coding.mdc**](rules/process-05-coding.mdc) - Universal coding practices

### Standards Files (Always Included)

- [**standards-user-story.mdc**](rules/standards-user-story.mdc) - Requirements phase standards
- [**standards-design.mdc**](rules/standards-design.mdc) - Design phase standards
- [**standards-task.mdc**](rules/standards-task.mdc) - Task creation standards
- [**standards-architecture.mdc**](rules/standards-architecture.mdc) - System architecture documentation
- [**standards-decision.mdc**](rules/standards-decision.mdc) - Architecture Decision Records (ADRs)
- [**standards-guidelines.mdc**](rules/standards-guidelines.mdc) - Guideline document standards

### Technology Guidelines (Conditional Inclusion)

Guidelines are supposed to be loaded automatically when you work with specific file types. These files are located in the `rules/` folder with `.mdc` extensions. There should be one `guidelines-{TOPIC}.mdc` document per topic.

### Detailed Guidelines Directory

The [**guidelines/{category}**](guidelines/) directory contains organized, detailed guidelines that are referenced by the rules files.

## Spec Workflow

The steering system supports a spec-driven development workflow:

1. **Requirements** - Use `@./rules/standards-user-story.mdc` for user story standards
2. **Design** - Use `@./rules/standards-design.mdc` for technical design standards
3. **Tasks** - Use `@./rules/standards-task.mdc` for implementation task standards
4. **Implementation** - Technology guidelines auto-load based on file types

## Usage Examples (using Cursor flavor inclusion syntax)

```bash
# Working on requirements
"Create requirements for user authentication @./rules/standards-user-story.mdc"

# Working on TypeScript implementation
# (guidelines-typescript.mdc automatically included when editing .ts files)

# Need architecture decision
"Should we use microservices? @./rules/standards-decision.mdc @./rules/standards-architecture.mdc"

# Working on verification and quality checks
"Are you actually following the instructions? Test out @./rules/guidelines-verification-protocol.mdc and see what your responses are."
```

## Initialization Scripts

Platform-specific setup scripts are provided to configure the necessary files for using these specs with different AI coding assistants.

### Available Scripts

- **`cursor-init.sh`** - Sets up genai-specs for Cursor IDE
- **`gemini-cli-init.sh`** - Sets up genai-specs for Gemini CLI

### Cursor IDE Setup (`cursor-init.sh`)

This script configures genai-specs for use with Cursor IDE:

1. **Submodule Verification**: Checks if the `.cursor` project is correctly configured as a Git submodule in your main repository
2. **Directory Structure**: Verifies the `.cursor/rules` and `.cursor/guidelines` directories exist
3. **Usage Instructions**: Provides guidance on how to reference rules in Cursor using `@./cursor/rules/filename.mdc`

### Gemini CLI Setup (`gemini-cli-init.sh`)

This script configures genai-specs for use with Gemini CLI:

1. **Submodule Verification**: Checks if the `genai-specs` project is correctly configured as a Git submodule in your main repository
2. **Environment File (`.env`) Management**: Creates `.env` file with placeholder variables (`GOOGLE_CLOUD_PROJECT`, `GEMINI_MODEL`, `GEMINI_API_KEY`)
3. **Gemini Settings File (`.gemini/settings.json`) Management**: Creates `.gemini/settings.json` with default configurations
4. **Git Ignore (`.gitignore`) Update**: Ensures `.env` is added to `.gitignore`

### How to Use

After adding genai-specs as a submodule to your main project, go to the genai-specs directory and run the appropriate script:

```bash
# For Cursor IDE
git submodule add git@github.com:betsalel-williamson/genai-specs.git .cursor
cd .cursor
./cursor-init.sh

# For Gemini CLI
git submodule add git@github.com:betsalel-williamson/genai-specs.git
cd genai-specs
./gemini-cli-init.sh
```

## Acknowledgements

This steering system and development methodology uses established practices and ideas from experts in software development:

### Spec-Driven Development

- **Pierce Boggan & Harald Kirschner** - Virtual workshop on spec-driven development
  [Microsoft Build Session BRK102](https://build.microsoft.com/en-US/sessions/BRK102)
- **Vivek Haldar** - Musings on spec-driven development
  [Spec-Driven Vibe Coding](https://vivekhaldar.com/articles/spec-driven-vibe-coding/)

### Test-Driven Development & Code Quality

- **Kent Beck** - Test-Driven Development (TDD) and "Tidy First" methodologies
  [Augmented Coding: Beyond the Vibes](https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes?open=false#§appendix-system-prompt)
- **Paul Hammond** - Comprehensive development practices and AI collaboration patterns
  [Claude Configuration](https://github.com/citypaul/.dotfiles/blob/main/claude/.claude/CLAUDE.md)
- **DORA Community** - Excellent documentation about software development best practices and community support.
  [Community Website](https://dora.community/)
  [DORA Practices Website](https://dora.dev)

### Engineering Principles

The core engineering principles combine best practices from:

- Continuous delivery and DevOps methodologies
- Domain-driven design patterns
- Functional programming principles
- Modern software architecture patterns

These ideas have been adapted and combined to create a unified system for AI-assisted development. This system maintains high code quality while enabling fast, iterative progress.
