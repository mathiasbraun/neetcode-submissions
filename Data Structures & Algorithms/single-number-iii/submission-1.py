class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        
        p = 0
        while xor & 1 == 0:
            xor = xor >> 1
            p += 1

        group_0 = []
        group_1 = []

        for n in nums:
            if (n >> p) & 1 == 0:
                group_0.append(n)
            else:
                group_1.append(n)
        return [self.singleNumberOne(group_0), self.singleNumberOne(group_1)]


    def singleNumberOne(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        return xor