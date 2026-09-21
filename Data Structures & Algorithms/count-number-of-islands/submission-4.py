class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set((i, j) for i in range(rows) for j in range(cols) if grid[i][j] == '1')
        count = 0

        while visit:
            pair = next(iter(visit))
            self.isLand(grid, pair[0], pair[1], visit)
            count += 1

        return count

    def isLand(self, grid: List[List[str]], r: int, c: int, visit) -> int:
        rows, cols = len(grid), len(grid[0])
        if (min(r, c) < 0                   # out of bounds left or top
            or r == rows or c == cols       # out of bounds bottom or right
            or (r, c) not in visit):
                return 0
        if grid[r][c] == '0':
            return 0
        
        land = 1

        visit.remove((r, c))
        land += self.isLand(grid, r + 1, c, visit)
        land += self.isLand(grid, r, c + 1, visit)
        land += self.isLand(grid, r - 1, c, visit)
        land += self.isLand(grid, r, c - 1, visit)

        return land