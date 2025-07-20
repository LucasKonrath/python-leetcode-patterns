from linkedLists import ListNode


def iterative_reversal(head: ListNode ) -> ListNode:
    curr_node, prev_node = head, None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node

def recursive_reversal(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new_head = recursive_reversal(head.next)
    head.next.next = head
    head.next = None

    return new_head