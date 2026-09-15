class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    # mergesort
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        res = []
        l, r = 0, 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

        if l < len(left):
            res += left[l:len(left)]
        if r < len(right):
            res += right[r:len(right)]

        return res

#    def sortArray(self, nums: List[int]) -> List[int]:
    # quicksort
#        if len(nums) <= 1:
#            return nums

#        l = 0
#        pivot = nums[len(nums) - 1]
#        for i in range(len(nums) - 1):
#            if nums[i] < pivot:
#                nums[l], nums[i] = nums[i], nums[l]
#                l += 1
#        nums[l], nums[len(nums) - 1] = nums[len(nums) - 1], nums[l]
        
#        left = self.sortArray(nums[:l])
#        right = self.sortArray(nums[l + 1:])

#        return left + [pivot] + right