import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from linkedLists.reverseLinkedList import iterative_reversal
import random

def make_linked_list(size):
    dummy = ListNode(0)
    curr = dummy
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
    return dummy.next

def benchmark_reverse_linked_list():
    head = make_linked_list(10000)
    t = timeit.timeit(lambda: iterative_reversal(head), number=10)
    print(f"iterative_reversal 10000 nodes (10 runs): {t:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"iterative_reversal 10000 nodes (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_reverse_linked_list()

