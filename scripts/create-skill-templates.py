#!/usr/bin/env python3
"""Create SDLC skill asset templates from migrated standards."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" / "sdlc"

TEMPLATES = {
    "spec-user-story/assets/user-story-template.md": """---
inclusion: manual
---

# {Feature Name} User Story

## User Persona

**Name:** {Persona Name}
**Description:** {Persona description, goals, pain points}

## User Story

**As a** {User Persona}
**I want to** {Action or Goal}
**so that** {Benefit or Value}

## Acceptance Criteria

- WHEN {user action/situation} THEN {user} SHALL {experience/achieve}

## Success Metrics

- **Primary Metric:** {verifiable pass/fail metric}
- **Secondary Metrics:** {additional verifiable metrics}
""",
    "spec-design/assets/design-template.md": """---
inclusion: manual
---

# {Feature Name} Design

## 1. Objective

{One-sentence goal linked to user story}

## 2. Technical Design

{High-level solution overview}

## 3. Key Changes

### 3.1. API Contracts

### 3.2. Data Models

### 3.3. Component Responsibilities

## 4. Alternatives Considered

## 5. Out of Scope
""",
    "spec-adr/assets/adr-template.md": """# ADR{NNNN}: {Title}

## Context

## Decision

## Alternatives Considered

## Consequences

## Rationale

## Status

proposed

## References
""",
    "spec-task-breakdown/assets/task-template.md": """---
inclusion: manual
---

# {Feature Name} Tasks

## Task 1: {Title}

**Objective:** {What code to write/modify}

**Acceptance Criteria:**

- {Verifiable outcome}

**Requirements Traceability:** {user story / design section}

**Test Strategy:** {How to verify}
""",
}

for rel, content in TEMPLATES.items():
    path = SKILLS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("Templates created.")
