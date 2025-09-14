# Genai Spec System Documentation

This directory contains a system for AI-assisted development. The system provides context-aware guidance that automatically includes relevant standards and guidelines based on the work being performed.

This project is designed to be imported as a Git submodule into other repositories.

This system is designed to be compatible with various agenic systems (e.g., Kiro, Gemini, Claude, Cursor) and provides a general set of instructions for spec-driven development.

## How the System Works

The system uses three inclusion strategies to provide efficient, relevant context:

- **Always Included**: Core principles that apply throughout all development work
- **Conditional Inclusion**: Technology-specific guidelines loaded based on file patterns
- **Manual Inclusion**: Specialized standards loaded on-demand using `#filename` in chat

## Directory Structure

### Core Process Files (Always Included)

- [**process-01-core.md**](steering/process-01-core.md) - Fundamental engineering principles
- [**process-02-project.md**](steering/process-02-project.md) - Project practices and spec driven workflow
- [**process-03-development.md**](steering/process-03-development.md) - TDD methodology and commit discipline  
- [**process-04-operational.md**](steering/process-04-operational.md) - Communication and quality standards
- [**process-05-coding.md**](steering/process-05-coding.md) - Universal coding practices

### Standards Files (Manual Inclusion)

Use `#filename` in chat to include these when needed:

- [**standards-user-story.md**](steering/standards-user-story.md) - Requirements phase standards
- [**standards-design.md**](steering/standards-design.md) - Design phase standards  
- [**standards-task.md**](steering/standards-task.md) - Task creation standards
- [**standards-architecture.md**](steering/standards-architecture.md) - System architecture documentation
- [**standards-decision.md**](steering/standards-decision.md) - Architecture Decision Records (ADRs)
- [**standards-guidelines.md**](steering/standards-guidelines.md) - Guideline document standards

### Technology Guidelines (Conditional Inclusion)

Automatically loaded based on file types being worked on. These are titled `guidelines-X.md`.

### Detailed Guidelines Directory

The [**guidelines/{category}**](guidelines/) directory contains organized, detailed guidelines referenced by the steering files:

## Spec Workflow

The steering system supports a general spec-driven development workflow:

1. **Requirements** - Use `#standards-user-story` for user story standards
2. **Design** - Use `#standards-design` for technical design standards
3. **Tasks** - Use `#standards-task` for implementation task standards
4. **Implementation** - Technology guidelines auto-load based on file types
5. **Review** - During testing, use `#guidelines-verification-protocol` to verify the agenic LLM system's behavior and validate its responses against expected outcomes based on the provided context. The `npm test` command should be used to perform these verification tests.

## Usage Examples

```bash
# Working on requirements
"Let's create requirements for user authentication #standards-user-story"

# Working on TypeScript implementation  
# (guidelines-typescript.md automatically included when editing .ts files)

# Need architecture decision
"Should we use microservices? #standards-decision #standards-architecture"

# Working on verification and quality checks
"Need to validate code quality #guidelines-verification-protocol"
```

## Initialization Script

The `init.sh` script located is designed to set up the necessary files for using these specs as a git submodule in your main project.

This script performs the following actions:

1.  **Submodule Verification**: Checks if the `genai-specs` project is correctly configured as a Git submodule in your main repository. If not, it will alert you and provide the `git submodule add ...` command to add it.
2.  **Environment File (`.env`) Management**:
    *   Creates a `.env` file in your main project's root directory if it doesn't already exist.
    *   Adds placeholder environment variables (`GOOGLE_CLOUD_PROJECT`, `GEMINI_MODEL`, `GEMINI_API_KEY`) to the `.env` file if they are missing. It will warn you if a variable already exists. See the Gemini CLI project for details on setting up a Google Cloud project and getting a Gemini API key.
3.  **Gemini Settings File (`.gemini/settings.json`) Management**:
    *   Creates the `.gemini` directory in your main project's root if it doesn't exist.
    *   Creates or updates `.gemini/settings.json` with default configurations for the Gemini CLI. If the file already exists and its content differs from the default, it will output a warning and show the differences, skipping the overwrite.
4.  **Git Ignore (`.gitignore`) Update**:
    *   Ensures that `.env` is added to your main project's `.gitignore` file to prevent sensitive information from being committed. It will create the `.gitignore` file if it doesn't exist.

### How to Use

To run the initialization script, after this project is added as a submodule project, navigate to the `genai-specs` directory within your main project and execute the script:

```bash
cd genai-specs
./init.sh
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

### Engineering Principles

The core engineering principles synthesize best practices from:

- Continuous delivery and DevOps methodologies
- Domain-driven design patterns
- Functional programming principles
- Modern software architecture patterns
- [DORA Community](https://dora.community/) and [best practices](https://dora.dev/guides/).

These influences have been adapted and integrated to create a cohesive system for AI-assisted development that maintains high code quality while enabling rapid, iterative progress.