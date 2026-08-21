#!/usr/bin/env python3
"""Convert genai-specs .mdc rules into Agent Skills."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules"
GUIDELINES = ROOT / "guidelines"
SKILLS = ROOT / "skills"

SDLc_MAP = {
    "standards-user-story.mdc": (
        "sdlc/spec-user-story",
        "spec-user-story",
        "Use when writing user stories, capturing requirements, defining personas, or drafting acceptance criteria for end-user value.",
        None,
    ),
    "standards-design.mdc": (
        "sdlc/spec-design",
        "spec-design",
        "Use when writing technical design documents, feature designs, or translating user stories into implementation approaches.",
        None,
    ),
    "standards-task.mdc": (
        "sdlc/spec-task-breakdown",
        "spec-task-breakdown",
        "Use when breaking features into tasks, writing task.md files, ACID step breakdowns, or planning incremental implementation work.",
        None,
    ),
    "standards-architecture.mdc": (
        "sdlc/spec-architecture",
        "spec-architecture",
        "Use when writing project-level architecture documents, C4 views, or system-wide structural documentation.",
        None,
    ),
    "standards-decision.mdc": (
        "sdlc/spec-adr",
        "spec-adr",
        "Use when recording architecture decisions, ADRs, trade-off analysis, or decision rationale for future teams.",
        None,
    ),
    "standards-guidelines.mdc": (
        "sdlc/spec-guideline-authoring",
        "spec-guideline-authoring",
        "Use when authoring new guideline documents, lessons learned entries, or sharded reference material in guidelines/.",
        None,
    ),
}

ENGINEERING_MAP = {
    "process-01-core.mdc": (
        "engineering/engineering-core-principles",
        "engineering-core-principles",
        "Use when making architecture, delivery, or engineering decisions, or when discussing scalability, reliability, or evidence-based claims.",
        None,
    ),
    "process-02-project.mdc": (
        "engineering/project-organization",
        "project-organization",
        "Use when organizing project files, documentation structure, .work-items layout, or spec artifact storage conventions.",
        None,
    ),
    "process-03-development.mdc": (
        "engineering/engineering-tdd-tidy-first",
        "engineering-tdd-tidy-first",
        "Use when implementing features, fixing bugs, or refactoring code where TDD, Tidy First, or commit discipline applies.",
        None,
    ),
    "process-04-operational.mdc": (
        "engineering/engineering-operational-protocols",
        "engineering-operational-protocols",
        "Use when modifying code with an AI assistant, reviewing generated code, or applying minimal-diff and communication standards.",
        None,
    ),
    "process-05-coding.mdc": (
        "engineering/engineering-coding-standards",
        "engineering-coding-standards",
        "Use when writing or reviewing application code across languages, designing functions, factories, or error handling patterns.",
        None,
    ),
}

VERIFICATION_MAP = {
    "guidelines-verification-protocol.mdc": (
        "verification/agent-verification-protocol",
        "agent-verification-protocol",
        "Use when designing agent evals, verifying TDD or Tidy First compliance, or building clean-room behavioral test scenarios.",
        None,
    ),
}

DOMAIN_MAP = {
    "guidelines-typescript.mdc": (
        "domains/typescript",
        "domain-typescript",
        "Use when writing, reviewing, or refactoring TypeScript or TSX code, types, modules, or TS-specific tests.",
        "**/*.{ts,tsx}",
        "typescript",
    ),
    "guidelines-javascript.mdc": (
        "domains/javascript",
        "domain-javascript",
        "Use when writing or reviewing JavaScript code, ES modules, or JS-specific patterns.",
        "**/*.js",
        "javascript",
    ),
    "guidelines-react.mdc": (
        "domains/react",
        "domain-react",
        "Use when writing or reviewing React components, hooks, JSX, or TSX UI code.",
        "**/*.{jsx,tsx}",
        "react",
    ),
    "guidelines-python.mdc": (
        "domains/python",
        "domain-python",
        "Use when writing or reviewing Python code or Python project conventions.",
        "**/*.py",
        "python",
    ),
    "guidelines-swift.mdc": (
        "domains/swift",
        "domain-swift",
        "Use when writing or reviewing Swift language code, concurrency, or Swift-specific patterns.",
        "**/*.swift",
        "swift",
    ),
    "guidelines-ios.mdc": (
        "domains/ios",
        "domain-ios",
        "Use when building SwiftUI views, iOS UI composition, or iOS-specific testing for Swift projects.",
        "**/*.swift",
        "ios",
    ),
    "guidelines-xcode.mdc": (
        "domains/xcode",
        "domain-xcode",
        "Use when debugging in Xcode, profiling performance, or configuring xcodebuild simulator destinations.",
        "**/*.swift",
        "xcode",
    ),
    "guidelines-docker.mdc": (
        "domains/docker",
        "domain-docker",
        "Use when writing Dockerfiles, container builds, image hardening, or Docker-based deployment workflows.",
        "**/{Dd}ocker*",
        "docker",
    ),
    "guidelines-github.mdc": (
        "domains/github",
        "domain-github",
        "Use when configuring GitHub Actions workflows, CI YAML, or Makefile-based GitHub automation.",
        ".github/**/*.yml,.github/**/*.yaml,Makefile",
        "github",
    ),
    "guidelines-pkl.mdc": (
        "domains/pkl",
        "domain-pkl",
        "Use when writing or reviewing Pkl configuration, templating, or Pkl language constructs.",
        "**/*.pkl",
        "pkl",
    ),
    "guidelines-highlightjs.mdc": (
        "domains/highlightjs",
        "domain-highlightjs",
        "Use when contributing Highlight.js language definitions or syntax highlighting for JS/TS code.",
        "**/*.{js,ts,jsx,tsx}",
        "highlightjs",
    ),
    "guidelines-testing.mdc": (
        "domains/testing",
        "domain-testing",
        "Use when writing tests, test strategy, BDD scenarios, or CSV/assertion patterns in test files.",
        "**/*.test.*",
        "testing",
    ),
}

CROSS_REFS = {
    "engineering-tdd-tidy-first": (
        "**REQUIRED SUB-SKILL:** Use `test-driven-development` for the Red-Green-Refactor cycle.\n"
    ),
    "spec-user-story": (
        "**REQUIRED SUB-SKILL:** Use `brainstorming` before creative requirements work.\n"
    ),
    "spec-design": (
        "**REQUIRED SUB-SKILL:** Use `brainstorming` when exploring design alternatives.\n"
    ),
    "spec-task-breakdown": (
        "**REQUIRED SUB-SKILL:** Use `writing-plans` when producing implementation plans from tasks.\n"
    ),
    "agent-verification-protocol": (
        "**REQUIRED SUB-SKILL:** Use `verification-before-completion` before claiming eval or migration success.\n"
    ),
}


def strip_frontmatter(content: str) -> str:
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3 :].lstrip("\n")
    return content


def split_evidence_section(body: str) -> tuple[str, str | None]:
    marker = "## Evidence-Based Engineering"
    if marker not in body:
        return body, None
    idx = body.index(marker)
    return body[:idx].rstrip() + "\n", body[idx:].rstrip() + "\n"


def split_cursor_plans_section(body: str) -> tuple[str, str | None]:
    marker = "## Active Work Tracking with Cursor Plans (Cursor-Specific)"
    if marker not in body:
        return body, None
    idx = body.index(marker)
    return body[:idx].rstrip() + "\n", body[idx:].rstrip() + "\n"


def insert_cross_ref(body: str, cross: str) -> str:
    if not cross:
        return body
    cross_block = f"\n## Required sub-skills\n\n{cross.strip()}\n"
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[: i + 1]) + cross_block + "\n" + "\n".join(lines[i + 1 :])
    return body + cross_block


def write_skill(
    rel_dir: str,
    name: str,
    description: str,
    body: str,
    paths: str | None = None,
    extra_files: dict[str, str] | None = None,
) -> None:
    skill_dir = SKILLS / rel_dir
    skill_dir.mkdir(parents=True, exist_ok=True)
    frontmatter = f"---\nname: {name}\ndescription: {description}\n"
    if paths:
        frontmatter += f'paths: "{paths}"\n'
    frontmatter += "---\n\n"
    cross = CROSS_REFS.get(name, "")
    content = frontmatter + insert_cross_ref(body, cross)
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    if extra_files:
        for rel_path, file_body in extra_files.items():
            target = skill_dir / rel_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(file_body, encoding="utf-8")


def migrate_rule_file(
    rule_name: str,
    rel_dir: str,
    skill_name: str,
    description: str,
    paths: str | None,
) -> None:
    source = RULES / rule_name
    body = strip_frontmatter(source.read_text(encoding="utf-8"))
    extra: dict[str, str] = {}

    if skill_name == "engineering-core-principles":
        main, evidence = split_evidence_section(body)
        body = main + (
            "\n## Evidence-Based Engineering\n\n"
            "See [references/evidence-based-engineering.md](references/evidence-based-engineering.md).\n"
        )
        if evidence:
            evidence = evidence.replace("## Evidence-Based Engineering", "# Evidence-Based Engineering", 1)
            extra["references/evidence-based-engineering.md"] = evidence

    if skill_name == "spec-task-breakdown":
        main, cursor = split_cursor_plans_section(body)
        body = main
        if cursor:
            cursor = cursor.replace(
                "## Active Work Tracking with Cursor Plans (Cursor-Specific)",
                "# Active Work Tracking with Cursor Plans (Cursor-Specific)",
                1,
            )
            cursor = re.sub(r"^### ", "## ", cursor, flags=re.M)
            extra["references/cursor-plan-bridge.md"] = cursor

    write_skill(rel_dir, skill_name, description, body, paths, extra or None)


def copy_guideline_refs(domain_key: str, skill_rel: str) -> None:
    src = GUIDELINES / domain_key
    if not src.is_dir():
        return
    dest = SKILLS / skill_rel / "references"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> None:
    for rule, (rel, name, desc, paths) in {**SDLc_MAP, **ENGINEERING_MAP, **VERIFICATION_MAP}.items():
        migrate_rule_file(rule, rel, name, desc, paths)

    for rule, (rel, name, desc, paths, guide_key) in DOMAIN_MAP.items():
        body = strip_frontmatter((RULES / rule).read_text(encoding="utf-8"))
        index_line = f"@../guidelines/{guide_key}/index.md"
        body = body.replace(index_line, f"See [references/index.md](references/index.md) for the full index.")
        body += (
            "\n\n## Progressive loading\n\n"
            "Read `references/index.md` first, then load individual reference files only when the task requires that topic.\n"
        )
        write_skill(rel, name, desc, body, paths)
        copy_guideline_refs(guide_key, rel)

    print("Migration complete.")


if __name__ == "__main__":
    main()
