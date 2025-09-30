# Genai Spec System Documentation

This directory contains a system for AI-assisted development. The system provides context-aware guidance that automatically includes relevant standards and guidelines based on the work being performed.

This project is designed to be imported as a Git submodule into other repositories.

This system is designed to be compatible with various agenic systems (e.g., Claude, Cursor, Gemini, Kiro) and provides a general set of instructions for spec-driven development.

## How the System Works

The system uses three inclusion strategies to provide efficient, relevant context:

- **Always Included**: Core principles that apply throughout all development work
- **Conditional Inclusion**: Technology-specific guidelines loaded based on file patterns
- **Manual Inclusion**: Specialized standards loaded on-demand using `@./rules/filename.mdc` in chat

## Directory Structure

### Core Process Files (Always Included)

- [**process-01-core.mdc**](rules/process-01-core.mdc) - Fundamental engineering principles
- [**process-02-project.mdc**](rules/process-02-project.mdc) - Project practices and spec driven workflow
- [**process-03-development.mdc**](rules/process-03-development.mdc) - TDD methodology and commit discipline  
- [**process-04-operational.mdc**](rules/process-04-operational.mdc) - Communication and quality standards
- [**process-05-coding.mdc**](rules/process-05-coding.mdc) - Universal coding practices

### Standards Files (Manual Inclusion)

Use `@./rules/filename.mdc` in chat to include these when needed:

- [**standards-user-story.mdc**](rules/standards-user-story.mdc) - Requirements phase standards
- [**standards-design.mdc**](rules/standards-design.mdc) - Design phase standards  
- [**standards-task.mdc**](rules/standards-task.mdc) - Task creation standards
- [**standards-architecture.mdc**](rules/standards-architecture.mdc) - System architecture documentation
- [**standards-decision.mdc**](rules/standards-decision.mdc) - Architecture Decision Records (ADRs)
- [**standards-guidelines.mdc**](rules/standards-guidelines.mdc) - Guideline document standards

### Technology Guidelines (Conditional Inclusion)

Automatically loaded based on file types being worked on. These are located in the `rules/` folder with `.mdc` extensions:

- [**guidelines-typescript.mdc**](rules/guidelines-typescript.mdc) - TypeScript development guidelines
- [**guidelines-javascript.mdc**](rules/guidelines-javascript.mdc) - JavaScript development guidelines
- [**guidelines-react.mdc**](rules/guidelines-react.mdc) - React development guidelines
- [**guidelines-python.mdc**](rules/guidelines-python.mdc) - Python development guidelines
- [**guidelines-docker.mdc**](rules/guidelines-docker.mdc) - Docker containerization guidelines
- [**guidelines-testing.mdc**](rules/guidelines-testing.mdc) - Testing methodology guidelines
- [**guidelines-pkl.mdc**](rules/guidelines-pkl.mdc) - PKL configuration guidelines
- [**guidelines-highlightjs.mdc**](rules/guidelines-highlightjs.mdc) - Highlight.js syntax guidelines
- [**guidelines-verification-protocol.mdc**](rules/guidelines-verification-protocol.mdc) - Verification and quality assurance guidelines

### Detailed Guidelines Directory

The [**guidelines/{category}**](guidelines/) directory contains organized, detailed guidelines referenced by the rules files:

## Spec Workflow

The steering system supports a general spec-driven development workflow:

1. **Requirements** - Use `@./rules/standards-user-story.mdc` for user story standards
2. **Design** - Use `@./rules/standards-design.mdc` for technical design standards
3. **Tasks** - Use `@./rules/standards-task.mdc` for implementation task standards
4. **Implementation** - Technology guidelines auto-load based on file types
5. **Review** - During testing, use `@./rules/guidelines-verification-protocol.mdc` to verify the agenic LLM system's behavior and validate its responses against expected outcomes based on the provided context. The `npm test` command should be used to perform these verification tests.

## Usage Examples

```bash
# Working on requirements
"Let's create requirements for user authentication @./rules/standards-user-story.mdc"

# Working on TypeScript implementation  
# (guidelines-typescript.mdc automatically included when editing .ts files)

# Need architecture decision
"Should we use microservices? @./rules/standards-decision.mdc @./rules/standards-architecture.mdc"

# Working on verification and quality checks
"Need to validate code quality @./rules/guidelines-verification-protocol.mdc"
```

## Initialization Scripts

Platform-specific initialization scripts are provided to set up the necessary files for using these specs with different AI coding assistants.

### Available Scripts

- **`cursor-init.sh`** - Sets up genai-specs for Cursor IDE
- **`gemini-cli-init.sh`** - Sets up genai-specs for Gemini CLI

### Cursor IDE Setup (`cursor-init.sh`)

This script sets up genai-specs for use with Cursor IDE:

1. **Submodule Verification**: Checks if the `.cursor` project is correctly configured as a Git submodule in your main repository
2. **Directory Structure**: Verifies the `.cursor/rules` and `.cursor/guidelines` directories exist
3. **Usage Instructions**: Provides guidance on how to reference rules in Cursor using `@./cursor/rules/filename.mdc`

### Gemini CLI Setup (`gemini-cli-init.sh`)

This script sets up genai-specs for use with Gemini CLI:

1. **Submodule Verification**: Checks if the `genai-specs` project is correctly configured as a Git submodule in your main repository
2. **Environment File (`.env`) Management**: Creates `.env` file with placeholder variables (`GOOGLE_CLOUD_PROJECT`, `GEMINI_MODEL`, `GEMINI_API_KEY`)
3. **Gemini Settings File (`.gemini/settings.json`) Management**: Creates `.gemini/settings.json` with default configurations
4. **Git Ignore (`.gitignore`) Update**: Ensures `.env` is added to `.gitignore`

### How to Use

After adding genai-specs as a submodule to your main project, navigate to the genai-specs directory and run the appropriate script:

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

This steering system and development methodology draws from established practices and thought leaders in software development:

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
- **DORA Community** - Amazing documentation about software development best practices as well as community support and encouragement.
  [Community Website](https://dora.community/)
  [DORA Practices Website](https://dora.dev)

### Engineering Principles

The core engineering principles synthesize best practices from:

- Continuous delivery and DevOps methodologies
- Domain-driven design patterns
- Functional programming principles
- Modern software architecture patterns

These influences have been adapted and integrated to create a cohesive system for AI-assisted development that maintains high code quality while enabling rapid, iterative progress.
