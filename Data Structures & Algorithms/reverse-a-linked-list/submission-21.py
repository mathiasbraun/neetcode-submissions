# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pred = None
        curr = head
        succ = curr.next
        while curr != None:
            succ = curr.next
            curr.next = pred
            pred = curr
            curr = succ
        return pred