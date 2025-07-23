import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from slidingwindow.substringAnagrams import substring_anagrams

class TestSubstringAnagrams(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(substring_anagrams("cbaebabacd", "abc"), 2)
        self.assertEqual(substring_anagrams("abab", "ab"), 3)
        self.assertEqual(substring_anagrams("a", "a"), 1)
        self.assertEqual(substring_anagrams("a", "b"), 0)

    def test_empty(self):
        self.assertEqual(substring_anagrams("", "a"), 0)
        self.assertEqual(substring_anagrams("a", ""), 0)
        self.assertEqual(substring_anagrams("", ""), 0)

    def test_longer_t_than_s(self):
        self.assertEqual(substring_anagrams("a", "abc"), 0)

    def test_repeated_characters(self):
        self.assertEqual(substring_anagrams("aaabbb", "ab"), 0)
        self.assertEqual(substring_anagrams("aaabbb", "aab"), 1)

if __name__ == "__main__":
    unittest.main()

