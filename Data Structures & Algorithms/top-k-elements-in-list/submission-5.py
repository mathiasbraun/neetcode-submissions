import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for key, value in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif value > heap[0][0]:
                heapq.heapreplace(heap, (value, key))

        return [h[1] for h in heap]