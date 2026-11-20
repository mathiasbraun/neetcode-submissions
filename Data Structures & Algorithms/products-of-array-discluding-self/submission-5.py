class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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

        return prod