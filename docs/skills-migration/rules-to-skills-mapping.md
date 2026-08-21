# Rules to Skills Mapping

Complete mapping from legacy `rules/*.mdc` to Agent Skills.

## Spec-flow (standards-*)

| Source rule | Skill name | Skill path | paths |
|-------------|------------|------------|-------|
| standards-user-story.mdc | spec-user-story | skills/sdlc/spec-user-story/ | — |
| standards-design.mdc | spec-design | skills/sdlc/spec-design/ | — |
| standards-task.mdc | spec-task-breakdown | skills/sdlc/spec-task-breakdown/ | — |
| standards-architecture.mdc | spec-architecture | skills/sdlc/spec-architecture/ | — |
| standards-decision.mdc | spec-adr | skills/sdlc/spec-adr/ | — |
| standards-guidelines.mdc | spec-guideline-authoring | skills/sdlc/spec-guideline-authoring/ | — |

## Engineering (process-*)

| Source rule | Skill name | Skill path | paths |
|-------------|------------|------------|-------|
| process-01-core.mdc | engineering-core-principles | skills/engineering/engineering-core-principles/ | — |
| process-02-project.mdc | project-organization | skills/engineering/project-organization/ | — |
| process-03-development.mdc | engineering-tdd-tidy-first | skills/engineering/engineering-tdd-tidy-first/ | — |
| process-04-operational.mdc | engineering-operational-protocols | skills/engineering/engineering-operational-protocols/ | — |
| process-05-coding.mdc | engineering-coding-standards | skills/engineering/engineering-coding-standards/ | — |

## Verification

| Source rule | Skill name | Skill path | paths |
|-------------|------------|------------|-------|
| guidelines-verification-protocol.mdc | agent-verification-protocol | skills/verification/agent-verification-protocol/ | — |

## Domain (guidelines-*)

| Source rule | Skill name | Skill path | paths |
|-------------|------------|------------|-------|
| guidelines-typescript.mdc | domain-typescript | skills/domains/typescript/ | `**/*.{ts,tsx}` |
| guidelines-javascript.mdc | domain-javascript | skills/domains/javascript/ | `**/*.js` |
| guidelines-react.mdc | domain-react | skills/domains/react/ | `**/*.{jsx,tsx}` |
| guidelines-python.mdc | domain-python | skills/domains/python/ | `**/*.py` |
| guidelines-swift.mdc | domain-swift | skills/domains/swift/ | `**/*.swift` |
| guidelines-ios.mdc | domain-ios | skills/domains/ios/ | `**/*.swift` |
| guidelines-xcode.mdc | domain-xcode | skills/domains/xcode/ | `**/*.swift` |
| guidelines-docker.mdc | domain-docker | skills/domains/docker/ | `**/{Dd}ocker*` |
| guidelines-github.mdc | domain-github | skills/domains/github/ | `.github/**/*.yml,.github/**/*.yaml,Makefile` |
| guidelines-pkl.mdc | domain-pkl | skills/domains/pkl/ | `**/*.pkl` |
| guidelines-highlightjs.mdc | domain-highlightjs | skills/domains/highlightjs/ | `**/*.{js,ts,jsx,tsx}` |
| guidelines-testing.mdc | domain-testing | skills/domains/testing/ | `**/*.test.*` |

Each domain skill includes `references/` copied from `guidelines/{stack}/`.

## Sharded references

| Skill | Reference file |
|-------|----------------|
| engineering-core-principles | references/evidence-based-engineering.md |
| spec-task-breakdown | references/cursor-plan-bridge.md |
