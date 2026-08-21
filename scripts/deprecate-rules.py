#!/usr/bin/env python3
"""Replace legacy .mdc rules with deprecation stubs pointing to skills."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules"

STUBS = {
    "standards-user-story.mdc": "skills/sdlc/spec-user-story",
    "standards-design.mdc": "skills/sdlc/spec-design",
    "standards-task.mdc": "skills/sdlc/spec-task-breakdown",
    "standards-architecture.mdc": "skills/sdlc/spec-architecture",
    "standards-decision.mdc": "skills/sdlc/spec-adr",
    "standards-guidelines.mdc": "skills/sdlc/spec-guideline-authoring",
    "process-01-core.mdc": "skills/engineering/engineering-core-principles",
    "process-02-project.mdc": "skills/engineering/project-organization",
    "process-03-development.mdc": "skills/engineering/engineering-tdd-tidy-first",
    "process-04-operational.mdc": "skills/engineering/engineering-operational-protocols",
    "process-05-coding.mdc": "skills/engineering/engineering-coding-standards",
    "guidelines-verification-protocol.mdc": "skills/verification/agent-verification-protocol",
    "guidelines-typescript.mdc": "skills/domains/domain-typescript",
    "guidelines-javascript.mdc": "skills/domains/domain-javascript",
    "guidelines-react.mdc": "skills/domains/domain-react",
    "guidelines-python.mdc": "skills/domains/domain-python",
    "guidelines-swift.mdc": "skills/domains/domain-swift",
    "guidelines-ios.mdc": "skills/domains/domain-ios",
    "guidelines-xcode.mdc": "skills/domains/domain-xcode",
    "guidelines-docker.mdc": "skills/domains/domain-docker",
    "guidelines-github.mdc": "skills/domains/domain-github",
    "guidelines-pkl.mdc": "skills/domains/domain-pkl",
    "guidelines-highlightjs.mdc": "skills/domains/domain-highlightjs",
    "guidelines-testing.mdc": "skills/domains/domain-testing",
}


def stub_for(skill_path: str, old_description: str) -> str:
    return f"""---
description: DEPRECATED — use {skill_path}/SKILL.md
alwaysApply: false
---

# Deprecated

This rule was migrated to an Agent Skill. Use `{skill_path}/SKILL.md` instead.

See [docs/skills-migration/rules-to-skills-mapping.md](../docs/skills-migration/rules-to-skills-mapping.md).

Original description: {old_description}
"""


for rule_name, skill_path in STUBS.items():
    path = RULES / rule_name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    desc = "Migrated rule"
    if text.startswith("---"):
        end = text.find("---", 3)
        block = text[3:end]
        for line in block.splitlines():
            if line.strip().startswith("description:"):
                desc = line.split(":", 1)[1].strip()
                break
    path.write_text(stub_for(skill_path, desc), encoding="utf-8")

print("Deprecation stubs written.")
