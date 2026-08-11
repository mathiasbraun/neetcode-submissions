class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        counter = 0
        for num in nums:
            if num == 1:
            # If 1 found, increase counter
                counter += 1
                if maximum < counter:
                # If counter > maximum, overwrite maximum with counter
                    maximum = counter
            else:
            # If 0 found, reset counter but keep maximum
                counter = 0
        return maximum