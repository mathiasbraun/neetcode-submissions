class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memoization(row: int, col: int, cache) -> int:
            if row == m or col == n:
                return 0
            if cache[row][col] > 0:
                return cache[row][col]
            if row == m - 1 and col == n - 1:
                return 1

            cache[row][col] = (memoization(row + 1, col, cache) 
                                + memoization(row, col + 1, cache))
            return cache[row][col]

        return memoization(0, 0, [[0] * n for i in range(m)])