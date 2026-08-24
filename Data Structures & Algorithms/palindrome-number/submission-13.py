class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = 0
        y = x
        while 10**p <= x:
            p += 1
        
        z = 0
        for i in range(p):
            coeff = (x // 10**((p - 1) - i)) % 10
            z += coeff * 10**i
            x -= coeff * 10**((p - 1) - i)

        return y == z