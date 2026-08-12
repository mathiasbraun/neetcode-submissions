# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # imagine head is on a 'middle' node with past and future
        if not head:
            return None
        save = head
        past = head
        fut = head.next
        while fut:
        # while there exists a subsequent node
            head = fut
            # move head one step forward
            fut = head.next
            # remember new future
            # has to be done before reversing
            # otherwise arrow from head to head.next will be lost
            head.next = past
            past = head
        save.next = None
        return head