class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        countZero = 0
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums