# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        cur = head
        N = 0
        while cur:
            cur = cur.next
            N += 1

        prev, cur = None, copy
        k = 0
        while k != N - n:
            tmp = cur
            cur = cur.next
            prev = tmp
            k += 1

        if not prev:
            return cur.next
        prev.next = cur.next
        return copy