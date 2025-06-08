import unittest
from app import check_credentials

class TestLogin(unittest.TestCase):

    def test_correct_credentials(self):
        self.assertTrue(check_credentials("admin", "1234"))

    def test_wrong_username(self):
        self.assertFalse(check_credentials("user", "1234"))

    def test_wrong_password(self):
        self.assertFalse(check_credentials("admin", "wrong"))

    def test_both_wrong(self):
        self.assertFalse(check_credentials("user", "wrong"))

if __name__ == '__main__':
    unittest.main()
