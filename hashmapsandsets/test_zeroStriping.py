import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from hashmapsandsets.zeroStriping import zero_striping_sets
import timeit

class TestZeroStripingSets(unittest.TestCase):
    def test_no_zeros(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 2], [3, 4]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_single_zero(self):
        matrix = [[1, 0], [3, 4]]
        expected = [[0, 0], [3, 0]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_multiple_zeros(self):
        matrix = [[0, 2], [3, 4]]
        expected = [[0, 0], [0, 4]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_all_zeros(self):
        matrix = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_single_row(self):
        matrix = [[1, 0, 3]]
        expected = [[0, 0, 0]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

    def test_single_column(self):
        matrix = [[1], [0], [3]]
        expected = [[0], [0], [0]]
        zero_striping_sets(matrix)
        self.assertEqual(matrix, expected)

class TestZeroStripingPerformance(unittest.TestCase):
    def test_performance(self):
        import random
        size = 300
        matrix = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]
        # Place a few zeros
        for i in range(0, size, 50):
            matrix[i][i] = 0
        t = timeit.timeit(lambda: zero_striping_sets(matrix), number=10)
        print(f"zero_striping_sets 300x300 matrix (10 runs): {t:.4f}s")
        with open("performance_results.txt", "a") as f:
            f.write(f"zero_striping_sets 300x300 matrix (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    unittest.main()

