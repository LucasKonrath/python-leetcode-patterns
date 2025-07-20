import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from fastandslow.linkedListCycleDetection import linked_list_cycle_detection
import random

def make_linked_list(size, cycle_pos=-1):
    dummy = ListNode(0)
    curr = dummy
    nodes = []
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
        nodes.append(curr)
    if cycle_pos != -1 and nodes:
        curr.next = nodes[cycle_pos]
    return dummy.next

def benchmark_linked_list_cycle_detection():
    # No cycle
    t_no_cycle = timeit.timeit(lambda: linked_list_cycle_detection(make_linked_list(10000)), number=10)
    # Cycle at start
    t_cycle = timeit.timeit(lambda: linked_list_cycle_detection(make_linked_list(10000, cycle_pos=0)), number=10)
    print(f"linked_list_cycle_detection 10000 nodes no cycle (10 runs): {t_no_cycle:.4f}s")
    print(f"linked_list_cycle_detection 10000 nodes with cycle (10 runs): {t_cycle:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"linked_list_cycle_detection 10000 nodes no cycle (10 runs): {t_no_cycle:.4f}s\n")
        f.write(f"linked_list_cycle_detection 10000 nodes with cycle (10 runs): {t_cycle:.4f}s\n")

if __name__ == "__main__":
    benchmark_linked_list_cycle_detection()

