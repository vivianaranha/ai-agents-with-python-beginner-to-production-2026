import sys, unittest
sys.path.insert(0,"src")
from agentpy.agent import Agent
from agentpy.providers import MockProvider
class TestAgent(unittest.TestCase):
    def test_mock_agent(self):
        out=Agent(MockProvider()).run("hello")
        self.assertEqual(out["status"],"done")
    def test_max_steps(self):
        class P:
            def generate(self,m): return '{"type":"noop"}'
        out=Agent(P(),max_steps=2).run("x")
        self.assertEqual(out["status"],"stopped")
