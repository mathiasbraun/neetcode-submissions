class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxFreq = 0
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > maxFreq:
                maxFreq = freq[n]

        for n in freq.keys():
            if freq[n] == maxFreq:
                return n