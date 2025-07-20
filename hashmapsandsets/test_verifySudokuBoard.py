import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from hashmapsandsets.verifySudokuBoard import verify_sudoku_board

class TestVerifySudokuBoard(unittest.TestCase):
    def test_valid_board(self):
        board = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertTrue(verify_sudoku_board(board))

    def test_invalid_row(self):
        board = [
            [5,3,3,0,7,0,0,0,0], # duplicate 3 in row
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertFalse(verify_sudoku_board(board))

    def test_invalid_column(self):
        board = [
            [5,3,0,0,7,0,0,0,0],
            [6,3,0,1,9,5,0,0,0], # duplicate 3 in column
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertFalse(verify_sudoku_board(board))

    def test_invalid_subgrid(self):
        board = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,5,0,0,0,0,6,0], # duplicate 5 in top-left subgrid
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.assertFalse(verify_sudoku_board(board))

    def test_empty_board(self):
        board = [[0]*9 for _ in range(9)]
        self.assertTrue(verify_sudoku_board(board))

if __name__ == "__main__":
    unittest.main()

