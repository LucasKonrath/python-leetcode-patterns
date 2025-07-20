def linked_list_intersection(headA, headB):
    first_pointer, second_pointer = headA, headB
    while first_pointer != second_pointer:
        first_pointer = first_pointer.next if first_pointer else headB
        second_pointer = second_pointer.next if second_pointer else headA
    return first_pointer
