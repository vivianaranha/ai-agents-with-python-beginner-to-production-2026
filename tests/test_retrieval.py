import sys, unittest
sys.path.insert(0,"src")
from agentpy.retrieval import retrieve
class TestRetrieval(unittest.TestCase):
    def test_retrieve(self):
        docs=["reset password using account settings","office cafeteria menu"]
        self.assertIn("password", retrieve("password reset",docs)[0])
