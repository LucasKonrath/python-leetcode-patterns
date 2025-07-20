import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from linkedLists.ListNode import ListNode
from linkedlistintersection.linkedListIntersection import linked_list_intersection
import random

def make_linked_list(size):
    dummy = ListNode(0)
    curr = dummy
    for i in range(size):
        curr.next = ListNode(random.randint(1, 10000))
        curr = curr.next
    return dummy.next

def benchmark_linked_list_intersection():
    # Create two lists with intersection at node 5000
    common = make_linked_list(5000)
    headA = make_linked_list(5000)
    headB = make_linked_list(3000)
    currA = headA
    while currA.next:
        currA = currA.next
    currA.next = common
    currB = headB
    while currB.next:
        currB = currB.next
    currB.next = common
    t = timeit.timeit(lambda: linked_list_intersection(headA, headB), number=10)
    print(f"linked_list_intersection (10,000 + 5,000 nodes) (10 runs): {t:.4f}s")
    with open("performance_results.txt", "a") as f:
        f.write(f"linked_list_intersection (10,000 + 5,000 nodes) (10 runs): {t:.4f}s\n")

if __name__ == "__main__":
    benchmark_linked_list_intersection()

