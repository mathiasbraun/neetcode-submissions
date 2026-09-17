class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in range(len(shift)):
            s = self.shift(s, shift[i])
        return s

    def shift(self, s: str, shift: List[int]) -> str:
        if shift[1] % len(s) == 0:
            return s
        
        if shift[1] < len(s):
            steps = shift[1]
        else:
            steps = shift[1] % len(s)

        if shift[0] == 0:
            return s[steps:] + s[:steps]
        elif shift[0] == 1:
            return s[-steps:] + s[:-steps]