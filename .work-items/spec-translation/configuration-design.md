---
inclusion: manual
---

# Spec Translation System - Configuration-Driven Approach

## 1. Objective

To create a simple, declarative configuration system that describes how each AI assistant handles file references, settings, and metadata, enabling automatic translation from the genai-specs standard format to any target platform.

## 2. Technical Design

The solution uses a configuration-driven approach where each AI assistant is defined by a simple JSON/YAML configuration that describes:

### Core Configuration Elements

- **File Reference Pattern**: How to reference rules and guidelines
- **Settings Location**: Where configuration files are stored
- **Metadata Handling**: How frontmatter and title matter is processed
- **Directory Structure**: Required directory layout
- **File Extensions**: Supported file types and extensions

### Configuration Schema

```yaml
# Example: cursor-config.yaml
platform: cursor
name: 'Cursor IDE'
version: '1.0'

file_references:
  pattern: '@{base_path}/{category}/{filename}'
  base_path: '.cursor'
  categories:
    rules: 'rules'
    guidelines: 'guidelines'
  examples:
    - '@.cursor/rules/standards-user-story.mdc'
    - '@.cursor/guidelines/typescript/index.md'

settings:
  location: '.cursor/rules'
  format: 'directory'
  file_extension: '.mdc'
  metadata_format: 'frontmatter'

metadata:
  frontmatter:
    enabled: true
    format: 'yaml'
    required_fields: ['description']
    optional_fields: ['alwaysApply', 'globs']

directory_structure:
  required:
    - '.cursor/rules'
    - '.cursor/guidelines'
  optional:
    - '.cursor'

init_script: 'cursor-init.sh'
```

### Translation Engine

The translation engine reads these configurations and:

1. **Parses genai-specs format** (rules + guidelines)
2. **Applies target platform configuration** to transform structure
3. **Generates appropriate files** in target format
4. **Creates directory structure** as specified
5. **Validates output** against platform requirements

## 3. Key Changes

### 3.1. API Contracts

- **Configuration Files**: Platform-specific YAML/JSON configurations
  - `configs/cursor.yaml` - Cursor platform configuration
  - `configs/gemini.yaml` - Gemini platform configuration
  - `configs/kiro.yaml` - Kiro platform configuration
  - `configs/claude.yaml` - Claude platform configuration

- **Translation Engine**: Generic engine that reads configurations
  - `translate-specs --platform cursor --input genai-specs --output .cursor`
  - `translate-specs --platform gemini --input genai-specs --output .gemini`

### 3.2. Data Models

- **Platform Configuration Schema**: Standardized format for describing AI assistant requirements
- **Translation Rules**: Mappings between genai-specs format and target platforms
- **Validation Schema**: Platform-specific validation rules

### 3.3. Component Responsibilities

- **Configuration Parser**: Reads and validates platform configurations
- **Translation Engine**: Applies configurations to transform genai-specs
- **File Generator**: Creates target platform files and directories
- **Validation Module**: Ensures output meets platform requirements

## 4. Configuration Examples

### Cursor Configuration

```yaml
platform: cursor
file_references:
  pattern: '@{base_path}/{category}/{filename}'
  base_path: '.cursor'
settings:
  location: '.cursor/rules'
  format: 'directory'
metadata:
  frontmatter:
    enabled: true
    format: 'yaml'
```

### Gemini Configuration

```yaml
platform: gemini
file_references:
  pattern: '#{filename}'
  base_path: ''
settings:
  location: '.gemini/settings.json'
  format: 'json'
metadata:
  frontmatter:
    enabled: false
    format: 'none'
```

### Kiro Configuration (Example)

```yaml
platform: kiro
file_references:
  pattern: 'include {filename}'
  base_path: 'configs'
settings:
  location: '.kiro/config.yaml'
  format: 'yaml'
metadata:
  frontmatter:
    enabled: true
    format: 'yaml'
```

## 5. Benefits

1. **Declarative**: Simple YAML/JSON describes each platform
2. **Extensible**: Easy to add new platforms
3. **Maintainable**: Changes to platform requirements only require config updates
4. **Testable**: Can validate configurations independently
5. **Reusable**: Same engine works for all platforms

## 6. Implementation Strategy

1. **Create configuration schema** and validation
2. **Build generic translation engine** that reads configurations
3. **Create platform configurations** for each AI assistant
4. **Integrate into init scripts** using the translation engine
5. **Add validation and testing** for each platform configuration
