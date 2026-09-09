import json
from typing import Protocol

class ModelProvider(Protocol):
    def generate(self, messages: list[dict]) -> str: ...

class MockProvider:
    """Deterministic offline provider for course labs."""
    def generate(self, messages: list[dict]) -> str:
        text = messages[-1].get("content", "") if messages else ""
        return json.dumps({"type":"final","answer":f"Mock response: {text[:120]}"})
