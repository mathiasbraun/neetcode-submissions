class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        for i in range(len(s)):
            if ord(s[i]) not in mapping:
                if ord(t[i]) in mapping.values():
                    return False
                else:
                    mapping[ord(s[i])] = ord(t[i])
            elif mapping[ord(s[i])] != ord(t[i]):
                return False

        return True