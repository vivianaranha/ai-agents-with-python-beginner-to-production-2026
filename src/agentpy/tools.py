from dataclasses import dataclass
from typing import Callable, Any
from .models import ToolResult

@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., Any]
    permission: str = "read"

    def call(self, **kwargs) -> ToolResult:
        try:
            return ToolResult(True, self.fn(**kwargs))
        except Exception as exc:
            return ToolResult(False, error=str(exc))

class ToolRegistry:
    def __init__(self): self._tools = {}
    def register(self, tool: Tool):
        if tool.name in self._tools: raise ValueError(f"duplicate tool: {tool.name}")
        self._tools[tool.name] = tool
    def get(self, name: str) -> Tool:
        if name not in self._tools: raise KeyError(name)
        return self._tools[name]
    def names(self): return sorted(self._tools)
