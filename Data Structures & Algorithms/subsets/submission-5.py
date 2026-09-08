class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]

        woLast = self.subsets(nums[:-1])
        wLast = [subset + [nums[-1]] for subset in woLast]
        return wLast + woLast