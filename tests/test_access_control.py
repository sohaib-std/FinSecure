import unittest
from security.access_control import AuthService

class TestAccessControl(unittest.TestCase):
    def test_authenticate_success(self):
        auth = AuthService()
        self.assertTrue(auth.authenticate("admin", "admin123"))

    def test_authenticate_failure(self):
        auth = AuthService()
        self.assertFalse(auth.authenticate("admin", "wrongpass"))

if __name__ == '__main__':
    unittest.main()