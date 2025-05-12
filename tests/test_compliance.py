import unittest
from services.compliance import Compliance

class TestCompliance(unittest.TestCase):
    def test_log_and_retrieve(self):
        comp = Compliance()
        comp.log_action("Test action")
        self.assertIn("Test action", comp.get_logs())

if __name__ == '__main__':
    unittest.main()