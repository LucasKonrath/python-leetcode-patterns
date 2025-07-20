import unittest
from hashmapsandsets.pairSumTwoSorted import pair_sum_unsorted_two_passes

class TestPairSumUnsortedTwoPasses(unittest.TestCase):
    def test_found_pair(self):
        self.assertEqual(sorted(pair_sum_unsorted_two_passes([2, 7, 11, 15], 9)), [0, 1])

    def test_no_pair(self):
        self.assertEqual(pair_sum_unsorted_two_passes([1, 2, 3], 7), [])

    def test_multiple_pairs(self):
        # Should return the first valid pair
        result = pair_sum_unsorted_two_passes([1, 2, 3, 4, 5], 5)
        self.assertTrue(result == [0, 3] or result == [1, 2])

    def test_empty_list(self):
        self.assertEqual(pair_sum_unsorted_two_passes([], 5), [])

    def test_single_element(self):
        self.assertEqual(pair_sum_unsorted_two_passes([5], 5), [])

    def test_duplicate_elements(self):
        self.assertEqual(sorted(pair_sum_unsorted_two_passes([3, 3], 6)), [0, 1])

if __name__ == "__main__":
    unittest.main()

