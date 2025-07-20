import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from linkedLists.ListNode import ListNode
from fastandslow.findLinkedListMiddleNode import findMiddle

class TestFindLinkedListMiddleNode(unittest.TestCase):
    def list_to_linked(self, lst):
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def test_empty_list(self):
        self.assertIsNone(findMiddle(None))

    def test_single_element(self):
        head = self.list_to_linked([1])
        self.assertEqual(findMiddle(head).val, 1)

    def test_two_elements(self):
        head = self.list_to_linked([1, 2])
        self.assertEqual(findMiddle(head).val, 2)

    def test_odd_length(self):
        head = self.list_to_linked([1, 2, 3, 4, 5])
        self.assertEqual(findMiddle(head).val, 3)

    def test_even_length(self):
        head = self.list_to_linked([1, 2, 3, 4, 5, 6])
        self.assertEqual(findMiddle(head).val, 4)

if __name__ == "__main__":
    unittest.main()

