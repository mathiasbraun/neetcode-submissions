class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        fib = [0, 1]
        i = 1
        while i <= n:
            tmp = fib[1]
            fib[1] = fib[0] + fib[1]
            fib[0] = tmp
            i += 1

        return fib[1]