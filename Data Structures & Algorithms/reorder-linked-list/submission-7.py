# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
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

        cur.next = None