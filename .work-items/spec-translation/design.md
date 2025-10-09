---
inclusion: manual
---

# Spec Translation System Design

## 1. Objective

To create a translation system that converts spec documents between different AI coding assistant formats (Cursor, Kiro, Gemini, Claude) while preserving the semantic meaning and structure of the rules and guidelines.

## 2. Technical Design

The proposed solution uses a configuration-driven approach that describes how each AI assistant handles file references, settings, and metadata. This enables automatic translation from the genai-specs standard format to any target platform through declarative configuration files.

### Core Configuration Elements

- **File Reference Pattern**: How to reference rules and guidelines (`@.cursor/rules/file.mdc` vs `#filename`)
- **Settings Location**: Where configuration files are stored (`.cursor/rules` vs `.gemini/settings.json`)
- **Metadata Handling**: How frontmatter and title matter is processed (YAML frontmatter vs JSON properties)
- **Directory Structure**: Required directory layout for each platform
- **File Extensions**: Supported file types and extensions

### Version Management Strategy

Since we don't control the external standards and APIs may change, the system uses version-specific configurations:

- **Version-Specific Configs**: `configs/cursor.v1.0.yaml`, `configs/gemini.v1.0.yaml`, etc.
- **Version Compatibility Matrix**: Clear documentation of which tool versions are supported
- **Brittleness Mitigation**: Fallback configurations and validation against known working examples
- **Community-Driven Discovery**: Reverse engineering from working examples rather than relying on potentially outdated documentation

### Core Components

- **Configuration-Driven Translation Engine**: Generic engine that reads platform configurations
- **Platform-Specific Init Scripts**: Each AI assistant gets its own init script that uses the translation engine
- **Version-Specific Configuration Files**: Declarative descriptions of how each platform version works
- **Validation Module**: Ensures translated specs maintain their intended functionality

### Architecture

```txt
genai-specs/
├── configs/                    # Version-specific platform configurations
│   ├── cursor.v1.0.yaml        # Cursor IDE v1.0 configuration
│   ├── gemini.v1.0.yaml        # Gemini CLI v1.0 configuration
│   ├── kiro.v1.0.yaml          # Kiro v1.0 configuration (when discovered)
│   └── claude.v1.0.yaml        # Claude v1.0 configuration (when discovered)
├── translate-specs.sh           # Generic translation engine
├── cursor-init.sh              # Uses translation engine for Cursor
├── kiro-init.sh                # Uses translation engine for Kiro
├── gemini-cli-init.sh          # Uses translation engine for Gemini
├── claude-init.sh              # Uses translation engine for Claude
├── rules/                      # Source genai-specs format
└── guidelines/                 # Detailed guidelines
```

### Translation Flow

1. **User runs platform-specific init script**: `./cursor-init.sh` or `./kiro-init.sh`
2. **Script detects genai-specs submodule**: Verifies rules and guidelines exist
3. **Script loads version-specific configuration**: Reads appropriate `configs/platform.vX.Y.yaml`
4. **Script calls translation engine**: Uses `translate-specs.sh` with platform config
5. **Translation engine applies configuration**: Converts genai-specs to platform-specific format
6. **Script creates platform files**: Generates appropriate config files and directory structure
7. **Script validates translation**: Ensures translated specs work with target platform

## 3. Key Changes

### 3.1. API Contracts

- **Translation Engine**: Generic engine that reads platform configurations
  - `translate-specs.sh --platform cursor --version 1.0 --input genai-specs --output .cursor`
  - `translate-specs.sh --platform gemini --version 1.0 --input genai-specs --output .gemini`

- **Init Script Interface**: Each platform init script uses the translation engine
  - `./cursor-init.sh` - Uses `configs/cursor.v1.0.yaml` to translate genai-specs to Cursor format
  - `./kiro-init.sh` - Uses `configs/kiro.v1.0.yaml` to translate genai-specs to Kiro format
  - `./gemini-cli-init.sh` - Uses `configs/gemini.v1.0.yaml` to translate genai-specs to Gemini format
  - `./claude-init.sh` - Uses `configs/claude.v1.0.yaml` to translate genai-specs to Claude format

### 3.2. Data Models

- **Platform Configuration Schema**: Declarative format for describing AI assistant requirements
- **Version-Specific Configurations**: Platform configurations tied to specific tool versions
- **Translation Rules**: Mappings between genai-specs format and target platforms
- **Validation Schema**: Platform-specific validation rules and compatibility matrices

### 3.3. Component Responsibilities

- **Translation Engine**: Generic engine that reads platform configurations and performs translations
- **Platform Init Scripts**: Handle submodule verification and call translation engine with appropriate config
- **Configuration Files**: Declarative descriptions of how each platform version handles file references, settings, and metadata
- **Validation Module**: Ensures translated specs maintain functionality with target platform versions

## 4. Alternatives Considered

- **Hardcoded Translation Logic**: Embedding platform-specific logic directly in init scripts. Rejected in favor of configuration-driven approach for better maintainability and extensibility.
- **API-Based Discovery**: Relying on official APIs or documentation. Rejected due to brittleness and lack of control over external standards.
- **Manual Conversion**: Manually recreating specs for each platform. Rejected due to maintenance overhead and potential inconsistencies.
- **Single Universal Format**: Creating one format that works everywhere. Rejected as different platforms have specific requirements and capabilities.
- **Platform-Specific Scripts**: Separate scripts for each conversion. Rejected in favor of unified configuration-driven approach for better maintainability.

## 5. Out of Scope

- Real-time synchronization between platforms
- Automatic format detection from existing projects
- Integration with specific AI assistant APIs
- Custom format creation beyond the supported platforms
- Automatic version detection and configuration selection
- Community-driven configuration discovery tools
