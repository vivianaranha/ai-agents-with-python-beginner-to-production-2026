# Capstone — Autonomous Operations Assistant

Build a production-oriented Python AI agent for an enterprise operations team.

## Required capabilities

- authenticated API boundary;
- typed request and response models;
- provider abstraction with offline/mock mode;
- bounded agent loop;
- at least four tools;
- permission checks per tool;
- retrieval over a supplied knowledge base;
- short-term memory plus explicit long-term-memory rules;
- planning for multi-step work;
- human approval for at least one risky action;
- MCP-style integration boundary;
- checkpoint/recovery behavior;
- evaluation dataset with at least 20 scenarios;
- adversarial/security tests;
- logs, traces and metrics;
- cost/latency budget;
- runbook and deployment architecture.

## Demo requirements

Demonstrate:

1. a successful grounded request;
2. a multi-tool request;
3. a denied high-risk action;
4. a prompt-injection attempt that does not gain tool authority;
5. a transient tool failure and recovery;
6. an evaluation report.

## Final repository

Your capstone should look like a small professional software product—not a notebook dump. Include architecture, setup, tests, evaluation, threat model, runbook and demo materials.
