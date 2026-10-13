class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        def memoization(r: int, c: int, cache) -> int:
            if r == m or c == n:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if cache[r][c] > 0:
                return cache[r][c]
            
            cache[r][c] = (memoization(r + 1, c, cache) + 
                            memoization(r, c + 1, cache))
            return cache[r][c]

        return memoization(0, 0, [[0] * n for i in range(m)])