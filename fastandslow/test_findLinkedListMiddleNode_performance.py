import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from fastandslow.findLinkedListMiddleNode import findMiddle
import random

def make_linked_list(size):
    dummy = ListNode(0)
    curr = dummy
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
    return dummy.next

def benchmark_find_middle():
    t = timeit.timeit(lambda: findMiddle(make_linked_list(10000)), number=10)
    print(f"findMiddle 10000 nodes (10 runs): {t:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"findMiddle 10000 nodes (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_find_middle()

