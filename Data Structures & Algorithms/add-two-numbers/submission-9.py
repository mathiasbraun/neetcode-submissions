# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        curr = head
        rest = 0

        while l1 or l2:
            if not l1:
                l1val = 0
                l2val = l2.val
            elif not l2:
                l1val = l1.val
                l2val = 0
            else:
                l1val = l1.val
                l2val = l2.val

            digit = (l1val + l2val + rest) % 10
            if l1val + l2val + rest >= 10:
                rest = 1
            else:
                rest = 0

            curr.next = ListNode(digit, None)
            curr = curr.next

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            elif l2:
                l2 = l2.next

        if rest == 1:
            curr.next = ListNode(1, None)
            curr = curr.next
            
        return head.next