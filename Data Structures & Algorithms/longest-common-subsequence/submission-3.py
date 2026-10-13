class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        matrix = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1

        def memoization(r: int, c: int, cache) -> int:
            best = 0
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1 if matrix[r][c] == 1 else 0
            if cache[r][c] > 0:
                return cache[r][c]

            if matrix[r][c] == 1:
                cache[r][c] = 1 + memoization(r + 1, c + 1, cache)
            else:
                cache[r][c] = max(memoization(r + 1, c, cache), 
                                memoization(r, c + 1, cache))

            return cache[r][c]

        return memoization(0, 0, [[0] * n for i in range(m)])