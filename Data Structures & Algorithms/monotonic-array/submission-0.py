class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        equ = 0
        inc = 0
        dec = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
            elif nums[i] > nums[i + 1]:
                dec += 1
            else:
                equ += 1
            if inc > 0 and dec > 0:
                return False
        return True
