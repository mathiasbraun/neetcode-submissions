class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        k = 0
        while k <= n:
            output += [self.countOnes(k)]
            k += 1
        return output

    def countOnes(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count