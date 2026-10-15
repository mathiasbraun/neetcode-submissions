class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        
        p = 0
        while xor & 1 == 0:
            xor = xor >> 1
            p += 1

        xor0 = 0
        xor1 = 0

        for n in nums:
            if (n >> p) & 1 == 0:
                xor0 = xor0 ^ n
            else:
                xor1 = xor1 ^ n
        return [xor0, xor1]