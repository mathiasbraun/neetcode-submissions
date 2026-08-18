class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head

        if index < 0:
            return -1
        elif index == 0:
            if curr is None:
                return -1
            else:
                return curr.val
        else:
            for i in range(index):
                if curr is None:
                    return -1
                curr = curr.next
            if curr is None:
                return -1
            return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head

        if curr == None:
            self.head = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node


    def remove(self, index: int) -> bool:
        curr = self.head

        if index < 0 or curr is None:
            return False
        else:
            if index == 0:
                self.head = curr.next
                return True
            else:
                for i in range(index - 1):
                    if curr is None:
                        return False
                    else:
                        curr = curr.next
                if curr is None:
                    return False
                else:
                    if curr.next is None:
                        return False
                    else:
                        curr.next = curr.next.next
                        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        
        return values
