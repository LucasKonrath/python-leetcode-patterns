import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from linkedLists.ListNode import ListNode
from fastandslow.linkedListCycleDetection import linked_list_cycle_detection

class TestLinkedListCycleDetection(unittest.TestCase):
    def list_to_linked(self, lst, cycle_pos=-1):
        dummy = ListNode(0)
        curr = dummy
        nodes = []
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
            nodes.append(curr)
        if cycle_pos != -1 and nodes:
            curr.next = nodes[cycle_pos]
        return dummy.next

    def test_no_cycle(self):
        head = self.list_to_linked([1, 2, 3, 4])
        self.assertFalse(linked_list_cycle_detection(head))

    def test_cycle_at_start(self):
        head = self.list_to_linked([1, 2, 3, 4], cycle_pos=0)
        self.assertTrue(linked_list_cycle_detection(head))

    def test_cycle_in_middle(self):
        head = self.list_to_linked([1, 2, 3, 4], cycle_pos=2)
        self.assertTrue(linked_list_cycle_detection(head))

    def test_single_node_no_cycle(self):
        head = self.list_to_linked([1])
        self.assertFalse(linked_list_cycle_detection(head))

    def test_single_node_with_cycle(self):
        head = self.list_to_linked([1], cycle_pos=0)
        self.assertTrue(linked_list_cycle_detection(head))

    def test_empty_list(self):
        self.assertFalse(linked_list_cycle_detection(None))

if __name__ == "__main__":
    unittest.main()

