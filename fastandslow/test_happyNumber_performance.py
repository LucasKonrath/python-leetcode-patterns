import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from fastandslow.happyNumber import happy_number
import random

def benchmark_happy_number():
    # Test a range of numbers for performance
    t = timeit.timeit(lambda: [happy_number(random.randint(1, 10000)) for _ in range(10000)], number=10)
    print(f"happy_number 10,000 random numbers (10 runs): {t:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"happy_number 10,000 random numbers (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_happy_number()

