from linkedLists.ListNode import ListNode


def remove_k_last_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy
    for _ in range(k):
        leader = leader.next
        if not leader:
            return head

    while leader.next:
        leader = leader.next
        trailer = trailer.next

    trailer.next = trailer.next.next
    return dummy.next