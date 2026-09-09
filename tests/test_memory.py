import sys, unittest
sys.path.insert(0,"src")
from agentpy.memory import MemoryStore
class TestMemory(unittest.TestCase):
    def test_active(self):
        m=MemoryStore(); m.add("hello"); self.assertIn("hello",m.active())
    def test_expired(self):
        m=MemoryStore(); m.add("gone",ttl_seconds=-1); self.assertNotIn("gone",m.active())
