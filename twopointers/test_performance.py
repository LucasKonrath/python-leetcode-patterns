import timeit
from twopointers.pairSumSorted import bruteForce, pairSumSorted
from twopointers.tripletSum import bruteForceTripletSum, tripletSumSorted
import random

def benchmark_pair_sum():
    nums = list(range(10000))
    target = 19999
    bf_time = timeit.timeit(lambda: bruteForce(nums, target), number=3)
    opt_time = timeit.timeit(lambda: pairSumSorted(nums, target), number=3)
    return bf_time, opt_time

def benchmark_triplet_sum():
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    bf_time = timeit.timeit(lambda: bruteForceTripletSum(nums), number=1)
    opt_time = timeit.timeit(lambda: tripletSumSorted(nums), number=1)
    return bf_time, opt_time

def main():
    bf_pair, opt_pair = benchmark_pair_sum()
    bf_triplet, opt_triplet = benchmark_triplet_sum()
    print(f"PairSum bruteForce: {bf_pair:.4f}s, pairSumSorted: {opt_pair:.4f}s")
    print(f"TripletSum bruteForce: {bf_triplet:.4f}s, tripletSumSorted: {opt_triplet:.4f}s")
    with open("performance_results.txt", "w") as f:
        f.write(f"PairSum bruteForce: {bf_pair:.4f}s, pairSumSorted: {opt_pair:.4f}s\n")
        f.write(f"TripletSum bruteForce: {bf_triplet:.4f}s, tripletSumSorted: {opt_triplet:.4f}s\n")

if __name__ == "__main__":
    main()

