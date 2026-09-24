class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0

        while p2 < len(abbr) and p1 < len(word):
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            elif 0 <= ord(abbr[p2]) - ord('a') <= 25:  
                # different lower case letters
                return False
            elif abbr[p2] == '0':
                return False
            else:
                i = p2
                strNum = ''
                while i < len(abbr) and not 0 <= ord(abbr[i]) - ord('a') <= 25:
                    strNum += abbr[i]
                    i += 1
                num = int(strNum)
                p1 += num
                p2 = i

        if not (p1 == len(word) and p2 == len(abbr)):
            return False
        return True
                