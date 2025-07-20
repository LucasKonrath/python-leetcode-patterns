import unittest
from twopointers.tripletSum import bruteForceTripletSum, tripletSumSorted

class TestBruteForceTripletSum(unittest.TestCase):
    def test_found_triplets(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = bruteForceTripletSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(result, expected)

    def test_no_triplets(self):
        nums = [1, 2, 3, 4]
        result = bruteForceTripletSum(nums)
        self.assertEqual(result, [])

    def test_empty_list(self):
        nums = []
        result = bruteForceTripletSum(nums)
        self.assertEqual(result, [])

    def test_less_than_three_elements(self):
        nums = [0, 1]
        result = bruteForceTripletSum(nums)
        self.assertEqual(result, [])

    def test_all_zeroes(self):
        nums = [0, 0, 0, 0]
        result = bruteForceTripletSum(nums)
        expected = [[0, 0, 0]]
        self.assertEqual(result, expected)

class TestTripletSumSorted(unittest.TestCase):
    def test_found_triplets(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = tripletSumSorted(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(result, expected)

    def test_no_triplets(self):
        nums = [1, 2, 3, 4]
        result = tripletSumSorted(nums)
        self.assertEqual(result, [])

    def test_empty_list(self):
        nums = []
        result = tripletSumSorted(nums)
        self.assertEqual(result, [])

    def test_less_than_three_elements(self):
        nums = [0, 1]
        result = tripletSumSorted(nums)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
