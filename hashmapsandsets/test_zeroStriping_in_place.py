import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from hashmapsandsets.zeroStriping import zero_striping_in_place

class TestZeroStripingInPlace(unittest.TestCase):
    def test_no_zeros(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 2], [3, 4]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_single_zero(self):
        matrix = [[1, 0], [3, 4]]
        expected = [[0, 0], [3, 0]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_multiple_zeros(self):
        matrix = [[0, 2], [3, 4]]
        expected = [[0, 0], [0, 4]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_all_zeros(self):
        matrix = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_single_row(self):
        matrix = [[1, 0, 3]]
        expected = [[0, 0, 0]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

    def test_single_column(self):
        matrix = [[1], [0], [3]]
        expected = [[0], [0], [0]]
        zero_striping_in_place(matrix)
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()

