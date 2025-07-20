import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import timeit
import random
from twopointers.largestContainer import largest_container_brute_force, largest_container_two_pointers

def benchmark_largest_container():
    heights = [random.randint(1, 10000) for _ in range(1000)]
    bf_time = timeit.timeit(lambda: largest_container_brute_force(heights), number=3)
    tp_time = timeit.timeit(lambda: largest_container_two_pointers(heights), number=3)
    print(f"LargestContainer brute_force: {bf_time:.4f}s, two_pointers: {tp_time:.4f}s")
    with open("twopointers/largest_container_performance.txt", "w") as f:
        f.write(f"LargestContainer brute_force: {bf_time:.4f}s, two_pointers: {tp_time:.4f}s\n")

if __name__ == "__main__":
    benchmark_largest_container()
