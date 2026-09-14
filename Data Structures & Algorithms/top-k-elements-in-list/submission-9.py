import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # bucket sort solution
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for c in range(len(freq) - 1, 0, -1):
            for n in freq[c]:
                res.append(n)
                if len(res) == k:
                    return res