import unittest
from services.crm import CRM

class TestCRM(unittest.TestCase):
    def test_create_customer(self):
        crm = CRM()
        result = crm.create_profile("Alice", "alice@example.com")
        self.assertEqual(result['name'], "Alice")

if __name__ == '__main__':
    unittest.main()