import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from fastandslow.happyNumber import happy_number

class TestHappyNumber(unittest.TestCase):
    def test_happy_number(self):
        self.assertTrue(happy_number(19))  # 19 is a happy number
        self.assertTrue(happy_number(1))   # 1 is a happy number
        self.assertTrue(happy_number(7))   # 7 is a happy number

    def test_unhappy_number(self):
        self.assertFalse(happy_number(2))  # 2 is not a happy number
        self.assertFalse(happy_number(4))  # 4 is not a happy number
        self.assertFalse(happy_number(20)) # 20 is not a happy number

    def test_edge_cases(self):
        self.assertTrue(happy_number(10))  # 10 is a happy number
        self.assertFalse(happy_number(0))  # 0 is not a happy number

if __name__ == "__main__":
    unittest.main()

