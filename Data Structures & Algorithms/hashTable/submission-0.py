class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None for i in range(capacity)]

    def insert(self, key: int, value: int) -> None:
        if self.map[key % self.capacity] == None:
            self.map[key % self.capacity] = [[key, value]]
        else:
            for i, pair in enumerate(self.map[key % self.capacity]):
                if pair[0] == key:
                    pair[1] = value
                    return
            self.map[key % self.capacity].append([key, value])
        self.size += 1
        if self.capacity <= 2 * self.size:
            self.resize()

    def get(self, key: int) -> int:
        if self.map[key % self.capacity] == None:
            return -1
        for pair in self.map[key % self.capacity]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> bool:
        if self.map[key % self.capacity] == None:
            return False
        for i, pair in enumerate(self.map[key % self.capacity]):
            if pair[0] == key:
                self.map[key % self.capacity].pop(i)
                self.size -= 1
                if len(self.map[key % self.capacity]) == 0:
                    self.map[key % self.capacity] = None
                return True
        return False            

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.size = 0
        self.capacity = 2 * self.capacity
        tmp = [None for i in range(self.capacity)]

        for oldpos in range(self.capacity // 2):
            if self.map[oldpos]:
                for i in range(len(self.map[oldpos])):
                    key = self.map[oldpos][i][0]
                    value = self.map[oldpos][i][1]
                    if tmp[key % self.capacity] == None:
                        tmp[key % self.capacity] = [[key, value]]
                    else:
                        tmp[key % self.capacity].append([key, value])
                    self.size += 1
        self.map = tmp