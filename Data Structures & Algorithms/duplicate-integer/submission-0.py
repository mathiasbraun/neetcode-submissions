# Solution with O(n log n) time, O(1) storage
# class Solution:
#    def hasDuplicate(self, nums: List[int]) -> bool:
#        nums.sort()
#        for i in range(len(nums)-1):
#            if nums[i+1] == nums[i]:
#                return True
#        return False

# Solution with O(n^2) time, O(1) storage
# class Solution:
#    def hasDuplicate(self, nums: List[int]) -> bool:
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] == nums[j]:
#                    return True
#        return False

# Solution with O(n) time, O(n) storage
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
        # O(n) time
            if num in seen:
            # O(1) time
                return True
            seen.add(num)
            # O(n) storage
        return False