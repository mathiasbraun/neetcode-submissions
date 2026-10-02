class Solution:
    def climbStairs(self, n: int) -> int:
        stair1, stair2 = 0, 1

        for i in range(n):
            tmp = stair2
            stair2 = stair1 + stair2
            stair1 = tmp

        return stair2