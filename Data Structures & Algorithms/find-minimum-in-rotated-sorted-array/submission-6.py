class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (r + l) // 2

        while l <= r:
            if nums[r] < nums[mid]:
                minimum = nums[r]
                l = mid + 1
                mid = (r + l) // 2
            else:
                if nums[l] > nums[mid]:
                    minimum = nums[mid]
                    l += 1
                    r = mid
                    mid = (r + l) // 2
                else:
                    minimum = nums[l]
                    r = mid - 1
                    mid = (r + l) // 2
                
        return minimum