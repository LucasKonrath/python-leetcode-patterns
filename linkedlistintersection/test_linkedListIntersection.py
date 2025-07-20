import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from linkedLists.ListNode import ListNode
from linkedlistintersection.linkedListIntersection import linked_list_intersection

class TestLinkedListIntersection(unittest.TestCase):
    def list_to_linked(self, lst):
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def test_no_intersection(self):
        headA = self.list_to_linked([1, 2, 3])
        headB = self.list_to_linked([4, 5, 6])
        self.assertIsNone(linked_list_intersection(headA, headB))

    def test_intersection(self):
        # Create intersection
        common = self.list_to_linked([7, 8])
        headA = self.list_to_linked([1, 2])
        headB = self.list_to_linked([3])
        # Attach common part
        currA = headA
        while currA.next:
            currA = currA.next
        currA.next = common
        currB = headB
        while currB.next:
            currB = currB.next
        currB.next = common
        self.assertIs(linked_list_intersection(headA, headB), common)

    def test_one_empty(self):
        headA = None
        headB = self.list_to_linked([1, 2, 3])
        self.assertIsNone(linked_list_intersection(headA, headB))

    def test_both_empty(self):
        self.assertIsNone(linked_list_intersection(None, None))

    def test_intersection_at_head(self):
        common = self.list_to_linked([1, 2, 3])
        self.assertIs(linked_list_intersection(common, common), common)

if __name__ == "__main__":
    unittest.main()

