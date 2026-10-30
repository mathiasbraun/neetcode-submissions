class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: slow and fast pointer meet 
        # somewhere inside the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: from the start and from the meeting point, 
        # one step each;
        # they meet at the cycle entry, which is the duplicate
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


        ''' Solution with O(n) time and O(n) space
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])'''