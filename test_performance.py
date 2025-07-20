import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import timeit
from twopointers.pairSumSorted import bruteForce, pairSumSorted
from twopointers.tripletSum import bruteForceTripletSum, tripletSumSorted
from twopointers.largestContainer import largest_container_brute_force, largest_container_two_pointers
from hashmapsandsets.pairSumTwoUnsorted import pair_sum_two_unsorted_two_pass, pair_sum_two_unsorted_one_pass
import random

def benchmark_pair_sum():
    nums = list(range(10000))
    target = 19999
    bf_time = timeit.timeit(lambda: bruteForce(nums, target), number=3)
    opt_time = timeit.timeit(lambda: pairSumSorted(nums, target), number=3)
    return bf_time, opt_time

def benchmark_triplet_sum():
    random.seed(42)
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    bf_time = timeit.timeit(lambda: bruteForceTripletSum(nums), number=1)
    opt_time = timeit.timeit(lambda: tripletSumSorted(nums), number=1)
    return bf_time, opt_time

def benchmark_largest_container():
    heights = [random.randint(1, 10000) for _ in range(1000)]
    bf_time = timeit.timeit(lambda: largest_container_brute_force(heights), number=3)
    tp_time = timeit.timeit(lambda: largest_container_two_pointers(heights), number=3)
    return bf_time, tp_time

def benchmark_pair_sum_unsorted():
    nums = [random.randint(1, 10000) for _ in range(10000)]
    target = nums[0] + nums[-1]
    two_pass_time = timeit.timeit(lambda: pair_sum_two_unsorted_two_pass(nums, target), number=3)
    one_pass_time = timeit.timeit(lambda: pair_sum_two_unsorted_one_pass(nums, target), number=3)
    return two_pass_time, one_pass_time

def main():
    bf_pair, opt_pair = benchmark_pair_sum()
    bf_triplet, opt_triplet = benchmark_triplet_sum()
    bf_container, tp_container = benchmark_largest_container()
    two_pass_unsorted, one_pass_unsorted = benchmark_pair_sum_unsorted()
    print(f"PairSum bruteForce: {bf_pair:.4f}s, pairSumSorted: {opt_pair:.4f}s")
    print(f"TripletSum bruteForce: {bf_triplet:.4f}s, tripletSumSorted: {opt_triplet:.4f}s")
    print(f"LargestContainer bruteForce: {bf_container:.4f}s, twoPointers: {tp_container:.4f}s")
    print(f"PairSumUnsorted two_pass: {two_pass_unsorted:.4f}s, one_pass: {one_pass_unsorted:.4f}s")
    with open("performance_results.txt", "w") as f:
        f.write(f"PairSum bruteForce: {bf_pair:.4f}s, pairSumSorted: {opt_pair:.4f}s\n")
        f.write(f"TripletSum bruteForce: {bf_triplet:.4f}s, tripletSumSorted: {opt_triplet:.4f}s\n")
        f.write(f"LargestContainer bruteForce: {bf_container:.4f}s, twoPointers: {tp_container:.4f}s\n")
        f.write(f"PairSumUnsorted two_pass: {two_pass_unsorted:.4f}s, one_pass: {one_pass_unsorted:.4f}s\n")

if __name__ == "__main__":
    main()
