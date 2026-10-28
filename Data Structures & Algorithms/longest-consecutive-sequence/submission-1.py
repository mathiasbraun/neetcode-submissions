class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occ = set(nums)
        longest = 0

        while occ:
            cur = occ.pop()
            length = 1
            x, y = cur - 1, cur + 1
            while x in occ:
                length += 1
                occ.discard(x)
                x -= 1
            while y in occ:
                length += 1
                occ.discard(y)
                y += 1
            longest = max(longest, length)

        return longest