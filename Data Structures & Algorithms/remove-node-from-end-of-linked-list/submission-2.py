# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        while n - 1:
            f = f.next
            n -= 1

        p, s = None, None
        while f:
            tmp = s
            f = f.next
            if s:
                s = s.next
            else:
                s = head
            p = tmp

        if not p:
            return s.next
        p.next = s.next
        return head

        


    ''' Solution with 2 iterations through the list
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
        return copy'''
