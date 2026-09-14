class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1

        while i > 1 and self.heap[i // 2] > self.heap[i]:
        # percolate up
            tmp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = tmp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        
        minimum = self.heap[1]

        self.heap[1] = self.heap[len(self.heap) - 1]
        # insert last element into root
        self.heap.pop()
        
        i = 1

        while 2 * i < len(self.heap):
        # percolate down
            if (2 * i + 1 < len(self.heap) and
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[i] > self.heap[2 * i + 1]):
            # swap if right child exists and is smaller than left and parent
                tmp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
            # swap if left child is smaller than parent
                tmp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i
            else:
            # no children or nothing to swap
                break

        return minimum

    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return

        self.heap = [0] + list(nums)
        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                # percolate down
                if (2 * i + 1 < len(self.heap) and
                        self.heap[2 * i + 1] < self.heap[2 * i] and
                        self.heap[i] > self.heap[2 * i + 1]):
                # swap if right child exists and is smaller than left and parent
                    tmp = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                # swap if left child is smaller than parent
                    tmp = self.heap[2 * i]
                    self.heap[2 * i] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i
                else:
                # no children or nothing to swap
                    break
            cur -= 1