class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' Solution with division
        p = 1
        numZeros = 0

        # Product without zeros
        for n in nums:
            if n != 0:
                p *= n
            else:
                numZeros += 1

        prod = [0] * len(nums)
        for i, n in enumerate(nums):
            if n == 0:
                if numZeros == 1:
                    prod[i] = p
            elif numZeros > 0:
                prod[i] = 0
            else:
                prod[i] = p // n

        return prod'''

        # Solution without division
        prodLeft = [1] * len(nums)
        prodRight = [1] * len(nums)
        for i in range(1, len(nums)):
            prodLeft[i] = prodLeft[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            prodRight[j] = prodRight[j + 1] * nums[j + 1]

        return [prodLeft[i] * prodRight[i] for i in range(len(nums))]