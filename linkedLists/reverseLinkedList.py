from linkedLists import ListNode


def iterative_reversal(head: ListNode ) -> ListNode:
    curr_node, prev_node = head, None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node