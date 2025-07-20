import unittest
from pairSumSorted import bruteForce, pairSumSorted

class TestPairSumSorted(unittest.TestCase):
    def test_found_pair(self):
        self.assertEqual(bruteForce([1, 2, 3, 4, 6], 6), [1, 3])

    def test_no_pair(self):
        self.assertEqual(bruteForce([1, 2, 3], 7), [])

    def test_multiple_pairs(self):
        # Should return the first valid pair
        self.assertEqual(bruteForce([1, 2, 3, 4, 5], 5), [0, 3])

    def test_empty_list(self):
        self.assertEqual(bruteForce([], 5), [])

    def test_single_element(self):
        self.assertEqual(bruteForce([5], 5), [])

    def test_pairSumSorted_found_pair(self):
        self.assertEqual(pairSumSorted([1, 2, 3, 4, 6], 6), [1, 3])

    def test_pairSumSorted_no_pair(self):
        self.assertEqual(pairSumSorted([1, 2, 3], 7), [])

    def test_pairSumSorted_multiple_pairs(self):
        self.assertEqual(pairSumSorted([1, 2, 3, 4, 5], 5), [0, 3])

    def test_pairSumSorted_empty_list(self):
        self.assertEqual(pairSumSorted([], 5), [])

    def test_pairSumSorted_single_element(self):
        self.assertEqual(pairSumSorted([5], 5), [])

if __name__ == "__main__":
    unittest.main()
