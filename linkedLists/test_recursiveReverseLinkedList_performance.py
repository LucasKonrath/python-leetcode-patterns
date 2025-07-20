import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from linkedLists.reverseLinkedList import recursive_reversal
import random

def make_linked_list(size):
    dummy = ListNode(0)
    curr = dummy
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
    return dummy.next

def benchmark_recursive_reverse_linked_list():
    t = timeit.timeit(lambda: recursive_reversal(make_linked_list(300)), number=10)
    print(f"recursive_reversal 300 nodes (10 runs): {t:.4f}s")
    with open("linkedLists/recursive_reverse_linked_list_performance.txt", "w") as f:
        f.write(f"recursive_reversal 300 nodes (10 runs): {t:.4f}s\n")
    with open("performance_results.txt", "a") as f:
        f.write(f"recursive_reversal 300 nodes (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_recursive_reverse_linked_list()
