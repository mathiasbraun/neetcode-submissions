class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        shortest = min(strs, key = len)

        if not shortest:
            return output

        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return output
            output += shortest[i]

        return output