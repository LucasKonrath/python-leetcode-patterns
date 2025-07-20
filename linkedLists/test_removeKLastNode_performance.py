import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from linkedLists.removeKLastNode import remove_k_last_node
import random

def make_linked_list(size):
    dummy = ListNode(0)
    curr = dummy
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
    return dummy.next

def benchmark_remove_k_last_node():
    t = timeit.timeit(lambda: remove_k_last_node(make_linked_list(10000), 5000), number=10)
    print(f"remove_k_last_node 10000 nodes, k=5000 (10 runs): {t:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"remove_k_last_node 10000 nodes, k=5000 (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_remove_k_last_node()

