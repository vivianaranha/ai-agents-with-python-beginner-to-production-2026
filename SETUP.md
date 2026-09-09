# Setup

## Recommended baseline

Use Python 3.12+ for the course. Python 3.14 is current in 2026, but 3.12/3.13 remain convenient classroom baselines when a third-party AI package has not yet caught up.

## Zero-dependency core path

The core `src/agentpy` package uses the Python standard library. This lets you learn agent engineering without dependency or API-key friction.

```bash
python --version
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows
python -m unittest discover -s tests -v
```

## Optional packages

Later modules may optionally use:

```bash
pip install fastapi uvicorn pydantic httpx pytest
```

Optional local-model path:

1. Install Ollama.
2. Pull a model you can run locally.
3. Set `AGENT_MODEL_PROVIDER=ollama`.
4. Keep provider-specific code behind the `ModelProvider` interface.

No exercise requires committing secrets. Copy `.env.example` when you add integrations.
