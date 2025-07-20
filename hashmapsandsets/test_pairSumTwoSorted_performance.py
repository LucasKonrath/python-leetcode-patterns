import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from hashmapsandsets.pairSumTwoUnsorted import pair_sum_two_unsorted_two_pass, pair_sum_two_unsorted_one_pass
import random

def benchmark_pair_sum_unsorted():
    nums = [random.randint(1, 10000) for _ in range(10000)]
    target = nums[0] + nums[-1]
    two_pass_time = timeit.timeit(lambda: pair_sum_two_unsorted_two_pass(nums, target), number=3)
    one_pass_time = timeit.timeit(lambda: pair_sum_two_unsorted_one_pass(nums, target), number=3)
    print(f"PairSumUnsorted two_pass: {two_pass_time:.4f}s, one_pass: {one_pass_time:.4f}s")
    with open("hashmapsandsets/pair_sum_unsorted_performance.txt", "w") as f:
        f.write(f"PairSumUnsorted two_pass: {two_pass_time:.4f}s, one_pass: {one_pass_time:.4f}s\n")
    # Add results to main performance_results.txt for CI comment aggregation
    with open("performance_results.txt", "a") as f:
        f.write(f"PairSumUnsorted two_pass: {two_pass_time:.4f}s, one_pass: {one_pass_time:.4f}s\n")

if __name__ == "__main__":
    benchmark_pair_sum_unsorted()
