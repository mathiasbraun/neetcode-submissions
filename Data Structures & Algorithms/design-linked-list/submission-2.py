class DoublyLinkedNode:

    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        if self.head is None:
            return -1
        else:
            curr = self.head
            # set current pointer at beginning of list
            for i in range(index):
                if curr is None:
                    return -1
                    # interrupt if list ends before index
                curr = curr.next
            if curr is None:
                return -1
                # above if condition does not check if index-th element is null
                # if it is, no value to extrapolate
            return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = DoublyLinkedNode(val, None, self.head)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = DoublyLinkedNode(val, self.tail, None)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        
        if self.head is None:
            if index > 0:
                return
            self.addAtHead(val)
            return
        
        curr = self.head

        for i in range(index):
            if curr is None:
                return
            curr = curr.next
        
        if curr is None:
            # if code runs until here, list has exactly index - 1 elements
            # so call addAtTail to insert node at the end
            self.addAtTail(val)
            return
        
        prec = curr.prev
        # if code runs until here, curr and curr.prev (which may be null) exist
        new_node = DoublyLinkedNode(val, prec, curr)
        prec.next = new_node
        curr.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return 
        
        if self.head is None:
            return

        curr = self.head

        for i in range(index):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return
        
        prec = curr.prev
        succ = curr.next

        if prec is None:
            self.head = succ
        else:
            prec.next = succ

        if succ is None:
            self.tail = prec
        else:
            succ.prev = prec



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)