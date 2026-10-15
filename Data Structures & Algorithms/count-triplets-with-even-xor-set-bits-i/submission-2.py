class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        count = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    count += 1 - self.parityBits(a[i] ^ b[j] ^ c[k])
        return count

    
    def parityBits(self, x: int) -> int:
        set_bits = 0
        while x > 0:
            if x & 1 == 1:
                set_bits +=1
            x = x >> 1
        rest = 0 if set_bits % 2 == 0 else 1
        return rest