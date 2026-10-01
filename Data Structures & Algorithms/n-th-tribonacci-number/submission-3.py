class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return min(n, 1)

        dp = [0, 1, 1]
        for i in range(3, n + 1):
            tmp = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = tmp

        return dp[2]