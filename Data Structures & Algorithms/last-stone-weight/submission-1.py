import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s1 != s2:
                heapq.heappush(maxHeap, -abs(s1 - s2))

        return 0 if not maxHeap else -maxHeap[0]