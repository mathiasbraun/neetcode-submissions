# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ''' Solution with O(n) time and O(n) space
    def reorderList(self, head: Optional[ListNode]) -> None:
        addr = {}
        cur = head
        i = 0
        while cur:
            addr[i] = cur
            cur = cur.next
            i += 1

        cur = addr[0]
        k = 0
        while k != i // 2:
            if k < i // 2:
                cur.next = addr[i - 1 - k]
                k = i - 1 - k
            else:
                cur.next = addr[i - k]
                k = i - k
            cur = cur.next

        cur.next = None'''

    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        s, r = head, head

        # End of iteration: s is the middle (odd length) or 
        # the last node of the first half (even length)
        while r.next and r.next.next:
            s = s.next
            r = r.next.next

        # Second half starts after s; cut the list there
        cur = s.next
        s.next = None

        # Reverse the second half
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        r = prev
        while p and r:
            tmpl = p.next
            tmpr = r.next
            p.next = r
            p = tmpl
            r.next = p
            r = tmpr



