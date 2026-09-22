class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            res = chr(ord('A') + digit) + res
        return res