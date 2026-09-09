# Project 13 — Reliable Production Agent Service

## Portfolio story

Add persistence, checkpoints, retries, idempotency, traces, metrics and cost controls.

## User problem

An operations team needs an assistant that reduces repetitive work without giving an LLM uncontrolled access to enterprise systems.

## Build steps

1. Write a one-paragraph problem statement and define the primary user.
2. List functional requirements and explicit non-goals.
3. Draw a simple architecture using Mermaid or ASCII.
4. Define typed input/output contracts.
5. Build the deterministic core first.
6. Add model-driven behavior behind an interface.
7. Add tools or retrieval only when they improve the user task.
8. Add validation, timeouts and safe error handling.
9. Add at least five automated tests.
10. Add an evaluation dataset with success criteria.
11. Threat-model the most important abuse case.
12. Add logs/traces for important decisions and tool calls.
13. Write a demo script with one success and one failure scenario.
14. Document deployment and next improvements.

## Required deliverables

- `README.md`
- `ARCHITECTURE.md`
- source code
- tests
- sample/synthetic data
- `EVALUATION.md`
- `SECURITY.md`
- `.env.example` if integrations are used
- demo script

## Acceptance criteria

The project must be reproducible, safe on malformed input, understandable by another developer and demonstrably testable. Irreversible actions must never be triggered only because a model emitted text that looked like a tool call.

## Interview questions

1. Why did you choose this agent boundary?
2. Which decisions are deterministic versus probabilistic?
3. What is the highest-risk tool or data source?
4. How do you evaluate success?
5. What would fail first at 100× traffic?
