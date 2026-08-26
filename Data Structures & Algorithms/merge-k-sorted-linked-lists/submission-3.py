# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # assume all optional lists are already ordered
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        # trivial cases done

        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])

        m = len(lists) // 2
        left = self.mergeKLists(lists[:m])
        right = self.mergeKLists(lists[m:])
        newlist = self.merge2Lists(left, right)

        return newlist

    def merge2Lists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left:
            return right
    
        if not right:
            return left

        dummy = ListNode()
        tail = dummy

        l = left
        r = right

        while l is not None and r is not None:
            if l.val <= r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next

            tail = tail.next

        if l is not None:
            tail.next = l
        else:
            tail.next = r

        return dummy.next       