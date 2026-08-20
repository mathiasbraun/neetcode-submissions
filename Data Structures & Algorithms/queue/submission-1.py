class ListNode:

    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        if self.tail is None:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            return
        
        new_node = ListNode(value, self.tail, None)
        self.tail.next = new_node
        # first append new node to queue, then move tail pointer
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        if self.head is None:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            return
        
        new_node = ListNode(value, None, self.head)
        self.head.prev = new_node
        # first append new node to queue, then move head pointer
        self.head = new_node

    def pop(self) -> int:
        if self.tail is None:
            return -1
        
        value = self.tail.val
        self.tail = self.tail.prev
        # move tail to second last node
        
        if self.tail is None:
        # if no second last node exists, list is empty, so need to modify head too
            self.head = None
            return value
        self.tail.next = None
        return value

    def popleft(self) -> int:
        if self.head is None:
            return -1
        
        value = self.head.val
        self.head = self.head.next
        # move head to second node

        if self.head is None:
        # if no second node exists, list is empty, so need to modify tail too
            self.tail = None
            return value
        self.head.prev = None
        return value
        
