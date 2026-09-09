from dataclasses import dataclass
from time import time

@dataclass
class MemoryItem:
    text: str
    created_at: float
    expires_at: float | None = None

class MemoryStore:
    def __init__(self): self._items = []
    def add(self, text: str, ttl_seconds: int | None = None):
        now=time(); exp=now+ttl_seconds if ttl_seconds else None
        self._items.append(MemoryItem(text, now, exp))
    def active(self):
        now=time(); return [x.text for x in self._items if x.expires_at is None or x.expires_at > now]
