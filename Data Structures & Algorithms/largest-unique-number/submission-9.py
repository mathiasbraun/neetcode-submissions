class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numList = {}
        for n in nums:
            numList[n] = numList.get(n, 0) + 1
        
        maxVal = -1
        for k, v in numList.items():
            if v == 1 and k > maxVal:
                maxVal = k

        return maxVal