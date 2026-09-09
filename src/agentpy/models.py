from dataclasses import dataclass, field
from typing import Any

@dataclass
class Task:
    task_id: str
    request: str
    user_id: str = "demo-user"
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class ToolResult:
    ok: bool
    value: Any = None
    error: str | None = None
