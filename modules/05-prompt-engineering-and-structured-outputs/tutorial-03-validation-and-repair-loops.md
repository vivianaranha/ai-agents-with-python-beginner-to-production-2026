# Tutorial 3: Validation and repair loops

## Goal

Learn **validation and repair loops** and apply it to a small part of a support-operations assistant.

## Why this matters for agents

AI agents combine probabilistic model behavior with deterministic software. The deterministic layer must validate data, control side effects, persist state, enforce permissions and recover from failure. This tutorial treats **validation and repair loops** as an engineering building block rather than an isolated Python topic.

## Prerequisites

- Complete the previous tutorial in this module.
- Use the course virtual environment.
- Keep secrets out of source code.

## Step 1 — Create the exercise folder

```bash
mkdir -p work/module-05/tutorial-3
cd work/module-05/tutorial-3
```

Create `main.py` and a `README.md` describing what you expect the program to do.

## Step 2 — Build the smallest deterministic version

Start without an LLM. Represent the input as ordinary Python data and produce a predictable output. The goal is to understand the contract before adding model behavior.

```python
from dataclasses import dataclass

@dataclass
class Task:
    task_id: str
    request: str
    risk: str = "low"


def process(task: Task) -> dict:
    if not task.request.strip():
        raise ValueError("request cannot be empty")
    return {"task_id": task.task_id, "status": "accepted", "risk": task.risk}


if __name__ == "__main__":
    print(process(Task("T-001", "Summarize the support queue")))
```

Run it:

```bash
python main.py
```

## Step 3 — Add the concept

Refactor the example so the program explicitly demonstrates **validation and repair loops**. Keep each function small. Give every function a clear input and output. Avoid hidden global state.

Ask yourself:

1. What data enters this component?
2. What assumptions are we making?
3. What can fail?
4. Which failures should stop the workflow?
5. What information should be logged?

## Step 4 — Add a failure case

Deliberately pass malformed or missing input. Do not only test the happy path.

```python
try:
    process(Task("T-002", ""))
except ValueError as exc:
    print(f"expected failure: {exc}")
```

## Step 5 — Add a test

Create `test_main.py`:

```python
import unittest
from main import Task, process

class TestProcess(unittest.TestCase):
    def test_accepts_valid_task(self):
        result = process(Task("T-1", "Check ticket status"))
        self.assertEqual(result["status"], "accepted")

    def test_rejects_empty_request(self):
        with self.assertRaises(ValueError):
            process(Task("T-2", ""))

if __name__ == "__main__":
    unittest.main()
```

Run:

```bash
python -m unittest -v
```

## Step 6 — Connect it to agent engineering

Write two sentences in your README explaining where this concept belongs in an agent architecture. Examples include request validation, tool contracts, state management, retries, approval logic, retrieval, API boundaries or observability.

## Step 7 — Production challenge

Improve the exercise with at least two of the following:

- type hints;
- explicit validation;
- structured logging;
- a timeout or retry boundary;
- an idempotency key;
- a permission check;
- a unit test for a second failure mode.

## Checkpoint

You should be able to explain the code without saying, “the AI handles it.” Identify exactly which behavior is deterministic and which behavior would eventually be delegated to a model.

## Common mistakes

- mixing model decisions with irreversible actions;
- accepting arbitrary dictionaries with no validation;
- catching every exception and silently continuing;
- storing secrets in source code;
- writing one large function that does prompting, tool calls, persistence and formatting.

## Mini challenge

Change the example from support operations to a domain you care about—sales, HR, finance, travel, education or IT—but preserve the same contract and tests.
