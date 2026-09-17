class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i, char in enumerate(keyboard):
            d[char] = i

        count = d[word[0]]
        for j in range(len(word) - 1):
            count += abs(d[word[j]] - d[word[j + 1]])

        return count