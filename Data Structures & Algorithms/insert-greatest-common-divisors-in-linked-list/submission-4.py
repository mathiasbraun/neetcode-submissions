# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            curVal = cur.val
            nextVal = cur.next.val
            newNode = ListNode(math.gcd(curVal, nextVal), cur.next)
            cur.next = newNode
            cur = cur.next.next

        return head