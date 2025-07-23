import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from slidingwindow.substringAnagrams import substring_anagrams
import random
import string

def benchmark_substring_anagrams():
    s = ''.join(random.choices(string.ascii_lowercase, k=10000))
    t = ''.join(random.choices(string.ascii_lowercase, k=5))
    t_time = timeit.timeit(lambda: substring_anagrams(s, t), number=10)
    print(f"substring_anagrams 10,000 chars, t=5 (10 runs): {t_time:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"substring_anagrams 10,000 chars, t=5 (10 runs): {t_time:.4f}s\n")

if __name__ == "__main__":
    benchmark_substring_anagrams()

