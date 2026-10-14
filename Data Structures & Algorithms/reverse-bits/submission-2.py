class Solution:
    def reverseBits(self, n: int) -> int:
        k = 0
        p = 31
        while n > 0:
            if n & 1 == 1:
                k += 1 << p
            n = n >> 1
            p -= 1
        return k