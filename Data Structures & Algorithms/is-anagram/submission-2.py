class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for letter in s:
            s_count[letter] = s_count.get(letter, 0) + 1
            # Runtime O(n)
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
            # Runtime O(m)
        if s_count == t_count:
            return True
        return False