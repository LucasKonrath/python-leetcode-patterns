import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from linkedLists.ListNode import ListNode
from linkedLists.reverseLinkedList import iterative_reversal

class TestReverseLinkedList(unittest.TestCase):
    def list_to_linked(self, lst):
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linked_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_empty_list(self):
        head = None
        self.assertIsNone(iterative_reversal(head))

    def test_single_element(self):
        head = self.list_to_linked([1])
        result = iterative_reversal(head)
        self.assertEqual(self.linked_to_list(result), [1])

    def test_multiple_elements(self):
        head = self.list_to_linked([1, 2, 3, 4])
        result = iterative_reversal(head)
        self.assertEqual(self.linked_to_list(result), [4, 3, 2, 1])

    def test_two_elements(self):
        head = self.list_to_linked([1, 2])
        result = iterative_reversal(head)
        self.assertEqual(self.linked_to_list(result), [2, 1])

if __name__ == "__main__":
    unittest.main()

