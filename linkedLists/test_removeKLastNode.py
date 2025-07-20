import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from linkedLists.ListNode import ListNode
from linkedLists.removeKLastNode import remove_k_last_node

class TestRemoveKLastNode(unittest.TestCase):
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

    def test_remove_last(self):
        head = self.list_to_linked([1, 2, 3, 4])
        result = remove_k_last_node(head, 1)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_remove_first(self):
        head = self.list_to_linked([1, 2, 3, 4])
        result = remove_k_last_node(head, 4)
        self.assertEqual(self.linked_to_list(result), [2, 3, 4])

    def test_remove_middle(self):
        head = self.list_to_linked([1, 2, 3, 4])
        result = remove_k_last_node(head, 2)
        self.assertEqual(self.linked_to_list(result), [1, 2, 4])

    def test_k_greater_than_length(self):
        head = self.list_to_linked([1, 2, 3])
        result = remove_k_last_node(head, 5)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_k_equals_length(self):
        head = self.list_to_linked([1, 2, 3])
        result = remove_k_last_node(head, 3)
        self.assertEqual(self.linked_to_list(result), [2, 3])

    def test_single_element(self):
        head = self.list_to_linked([1])
        result = remove_k_last_node(head, 1)
        self.assertEqual(self.linked_to_list(result), [])

    def test_empty_list(self):
        head = None
        result = remove_k_last_node(head, 1)
        self.assertEqual(self.linked_to_list(result), [])

if __name__ == "__main__":
    unittest.main()

