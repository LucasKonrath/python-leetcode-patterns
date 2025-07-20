import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from hashmapsandsets.zeroStriping import zero_striping_sets
import random

def benchmark_zero_striping():
    size = 300
    matrix = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]
    for i in range(0, size, 50):
        matrix[i][i] = 0
    t = timeit.timeit(lambda: zero_striping_sets(matrix), number=10)
    print(f"zero_striping_sets 300x300 matrix (10 runs): {t:.4f}s")
    with open("hashmapsandsets/zero_striping_performance.txt", "w") as f:
        f.write(f"zero_striping_sets 300x300 matrix (10 runs): {t:.4f}s\n")
    with open("performance_results.txt", "a") as f:
        f.write(f"zero_striping_sets 300x300 matrix (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_zero_striping()

