class Solution:
    def climbStairs_recursive(self, n: int) -> int:
        if n in {1, 2}:
        # if only 1 or 2 steps, correspondingly 1 or 2 distinct ways
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # if at step n - 1, only 1 way
        # if at step n - 2, can either go directly to n or to n - 1
    
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one