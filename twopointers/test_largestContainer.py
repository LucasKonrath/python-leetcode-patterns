import unittest
from twopointers.largestContainer import largest_container_brute_force

class TestLargestContainer(unittest.TestCase):
    def test_example(self):
        self.assertEqual(largest_container_brute_force([1,8,6,2,5,4,8,3,7]), 49)

    def test_empty(self):
        self.assertEqual(largest_container_brute_force([]), 0)

    def test_single_element(self):
        self.assertEqual(largest_container_brute_force([5]), 0)

    def test_two_elements(self):
        self.assertEqual(largest_container_brute_force([1, 1]), 1)

    def test_all_same_height(self):
        self.assertEqual(largest_container_brute_force([3,3,3,3]), 9)

    def test_decreasing_heights(self):
        self.assertEqual(largest_container_brute_force([5,4,3,2,1]), 6)

    def test_increasing_heights(self):
        self.assertEqual(largest_container_brute_force([1,2,3,4,5]), 6)

if __name__ == "__main__":
    unittest.main()

