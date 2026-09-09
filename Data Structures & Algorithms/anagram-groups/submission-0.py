from typing import Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col = {}

        for s in strs:
            perm = self.getLetterFreq(s)
            if perm not in col.keys():
                col[perm] = [s]
            else:
                col[perm].append(s)
        
        return [col[perm] for perm in col.keys()]



    def getLetterFreq(self, s: str) -> tuple[int]:
        res = [0] * 26

        for char in s:
            res[ord(char) - ord('a')] += 1
        
        return tuple(res)