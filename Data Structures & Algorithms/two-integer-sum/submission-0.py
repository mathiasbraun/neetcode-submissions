class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i in range(len(nums)):
            if target - nums[i] in memory:
                return[memory[target - nums[i]], i]
            memory[nums[i]] = i
        return False