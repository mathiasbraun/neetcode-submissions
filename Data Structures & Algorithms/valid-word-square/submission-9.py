class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if len(words[i]) <= j:
                    wij = ' '
                else:
                    wij = words[i][j]
                if j >= len(words) or len(words[j]) <= i:
                    wji = ' '
                else:
                    wji = words[j][i]
                if wij != wji:
                    return False
        return True