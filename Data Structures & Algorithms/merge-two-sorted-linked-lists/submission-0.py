# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoNonemptyLists(self, list1, list2):
        head = None
        current = None
        l1 = list1
        l2 = list2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                chosen = l1
                l1 = l1.next
            else:
                chosen = l2
                l2 = l2.next
            if head is None:
                head = chosen
                current = chosen
            else:
                current.next = chosen
                current = chosen
        # eine der Listen ist jetzt leer — den Rest der anderen anhängen
        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        return head


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            if list2 == None:
                return None
            else:
                return list2
        if list2 == None:
            return list1
        return self.mergeTwoNonemptyLists(list1, list2)