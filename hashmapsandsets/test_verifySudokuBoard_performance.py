import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from hashmapsandsets.verifySudokuBoard import verify_sudoku_board
import random

def benchmark_verify_sudoku_board():
    # Generate a large number of valid boards for benchmarking
    board = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
    # Make sure the board is valid by setting all to zero (fastest case)
    empty_board = [[0]*9 for _ in range(9)]
    valid_time = timeit.timeit(lambda: verify_sudoku_board(board), number=100)
    empty_time = timeit.timeit(lambda: verify_sudoku_board(empty_board), number=100)
    print(f"verify_sudoku_board random board: {valid_time:.4f}s, empty board: {empty_time:.4f}s")
    with open("hashmapsandsets/verify_sudoku_board_performance.txt", "w") as f:
        f.write(f"verify_sudoku_board random board: {valid_time:.4f}s, empty board: {empty_time:.4f}s\n")
    # Also append to main performance_results.txt for CI aggregation
    with open("performance_results.txt", "a") as f:
        f.write(f"verify_sudoku_board random board: {valid_time:.4f}s, empty board: {empty_time:.4f}s\n")

if __name__ == "__main__":
    benchmark_verify_sudoku_board()

