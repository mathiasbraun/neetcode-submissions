class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        y = x
        while abs(y * y - x) >= 0.5:
            y = y / 2 + (x / y) / 2
        return int(y)