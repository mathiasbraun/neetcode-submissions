class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVol = (r - l) * min(heights[l], heights[r])

        while l < r:
            currVol = (r - l) * min(heights[l], heights[r])
            if currVol > maxVol:
                maxVol = currVol
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return maxVol