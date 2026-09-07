class Solution:
    def confusingNumber(self, n: int) -> bool:
        rot = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        length = len(str(n))
        i = 0
        nConf = 0

        while i < length:
            digit = (n // 10**i) % 10
            if digit not in rot:
                return False
            else:
                nConf += rot[digit] * 10**(length - i - 1)
            i += 1

        return not n == nConf