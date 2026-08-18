class ListNode:
    # initiate environment for node
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        # initialization of pointer at null
    
    def get(self, index: int) -> int:
        curr = self.head

        if index < 0:
            return -1
            # return -1 if index invalid
        elif index == 0:
            if curr is None:
                return -1
                # return -1 if list is empty
            else:
                return curr.val
                # return value of head in the index = 0 case
        else:
            for i in range(index):
            # run through the list
                if curr is None:
                # if we happen to meet the tail before index, return -1
                    return -1
                curr = curr.next
                # update curr, one step further
            if curr is None:
                return -1
                # return -1 if we have arrived at null
            return curr.val
            # otherwise return value of node

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        # create new node with value val
        new_node.next = self.head
        # set next to original head
        self.head = new_node
        # set new head to point at new node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head

        if curr == None:
            self.head = new_node
            # if list is empty, simply change pointer to new node
        else:
            while curr.next is not None:
                curr = curr.next
                # go through list as long as next is not null
            curr.next = new_node
            # append new node


    def remove(self, index: int) -> bool:
        curr = self.head

        if index < 0 or curr is None:
        # return false if index out of bounds or nothing to remove
            return False
        else:
            if index == 0:
            # if head to remove, set self.head to curr.next
                self.head = curr.next
                return True
            else:
                for i in range(index - 1):
                # go through the list until the element BEFORE the i-th
                    if curr is None:
                    # break if we find end of list along the way
                        return False
                    else:
                        curr = curr.next
                        # move curr pointer one step further
                if curr is None:
                # if pointer BEFORE i-th is null, end of list reached
                    return False
                else:
                    if curr.next is None:
                    # if i-th is null, nothing to remove at i-th position
                        return False
                    else:
                        curr.next = curr.next.next
                        # overwrite curr.next with successor of curr.next
                        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        
        return values
