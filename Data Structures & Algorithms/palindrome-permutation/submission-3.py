class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        count = 0
        for v in freq.values():
            if v % 2 == 1:
                count += 1
            if count > 1:
                return False

        return True