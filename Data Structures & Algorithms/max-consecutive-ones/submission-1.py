class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
                if maximum < counter:
                    maximum = counter
            else:
                counter = 0
        return maximum