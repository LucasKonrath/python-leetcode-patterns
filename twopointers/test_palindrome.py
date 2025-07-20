import unittest
from twopointers.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("aba"))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("abba"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("abc"))

    def test_case_sensitive(self):
        self.assertFalse(is_palindrome("Abba"))

if __name__ == "__main__":
    unittest.main()

