import sys, unittest
sys.path.insert(0, "src")
from agentpy.tools import Tool, ToolRegistry

class TestTools(unittest.TestCase):
    def test_registry(self):
        r=ToolRegistry(); r.register(Tool("add","add",lambda a,b:a+b))
        self.assertEqual(r.get("add").call(a=2,b=3).value,5)
    def test_duplicate(self):
        r=ToolRegistry(); r.register(Tool("x","x",lambda:1))
        with self.assertRaises(ValueError): r.register(Tool("x","x",lambda:2))
