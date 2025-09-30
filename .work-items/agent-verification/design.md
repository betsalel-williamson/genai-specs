---
inclusion: manual
---

# Agent Verification System Design

## 1. Objective

To design a conceptual framework for an external system capable of verifying the behavior of agenic LLM systems (e.g., Gemini CLI) against expected responses, using contextual documents like `guidelines-verification-protocol.md`.

## 2. Technical Design

The proposed solution involves an external testing framework that operates independently of the `genai-specs` repository. This framework will programmatically interact with the target agenic LLM system, provide specific prompts and contextual files, capture the agent's output, and then assert that the output meets predefined expectations.

The core components of this external system would include:

* **Test Runner**: An `npm` based test runner (e.g., Jest, Mocha) to orchestrate test execution.
* **Agent Invocation Module**: A module responsible for programmatically calling the target agenic LLM system. This would involve:
  * Constructing prompts with embedded context (e.g., `#steering/guidelines-verification-protocol.md`).
  * Executing the agent command (e.g., `gemini-cli "What are the core verification areas? #steering/guidelines-verification-protocol.md"`).
  * Capturing the standard output of the agent.
* **Assertion Module**: A module that takes the captured agent output and compares it against expected responses using assertion libraries. This would involve parsing the agent's response to extract relevant information for comparison.

This design is informed by the principles of automated testing and the need for a reproducible verification process for AI agents.

## 3. Key Changes

This design document outlines an *external* system and does not propose direct changes to the `genai-specs` repository's codebase or API contracts. The `package.json` `test` script has been updated to reflect the conceptual nature of this verification.

### 3.1. API Contracts

N/A - No new or modified API endpoints within this project.

### 3.2. Data Models

N/A - No new or modified database schemas or data structures within this project.

### 3.3. Component Responsibilities

* **External Test Runner**: Orchestrates the execution of verification tests.
* **Agent Invocation Module**: Responsible for interacting with the agenic LLM system, providing prompts and context, and capturing output.
* **Assertion Module**: Responsible for evaluating the captured agent output against expected results.

## 4. Alternatives Considered

* **Manual Verification**: Relying solely on manual inspection of agent responses. This was rejected due to its lack of scalability, reproducibility, and efficiency for continuous integration.
* **In-Agent Self-Testing**: Attempting to have the agent test itself from within its own execution environment. This was deemed impractical due to the inherent limitations of an agent testing its own live, interactive process.

## 5. Out of Scope

* Specific test cases or expected outputs for agent behavior.
