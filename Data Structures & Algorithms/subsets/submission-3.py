class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]

        woFirst = self.subsets(nums[1:])
        wFirst = [subset + [nums[0]] for subset in woFirst]
        return wFirst + woFirst
        