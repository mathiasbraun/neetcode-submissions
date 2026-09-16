class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0
        best = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                length += 1
            else:
                for i in range(l, r):
                    seen.remove(s[i])
                    length -= 1
                    if s[i] == s[r]:
                        l = i + 1
                        break
            best = max(best, length)

        return best