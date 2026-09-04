class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        for i in range(len(t)):
            if s:
                if t[i] == s[0]:
                    s = s[1:]

        return not s

