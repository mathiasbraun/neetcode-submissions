class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())

    def dfs(self, grid: List[List[int]], r: int, c: int, visit) -> int:
        rows, cols = len(grid), len(grid[0])
        if ((r,c) in visit                  # node already visited
            or min(r, c) < 0                # we step outside grid left or above
            or r == rows or c == cols):     # we step outsice grid right or below
            return 0
        if grid[r][c] == 1:
            return 0                        # we are not allowed to visit ones
        if r == rows - 1 and c == cols - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += self.dfs(grid, r + 1, c, visit)
        count += self.dfs(grid, r, c + 1, visit)
        count += self.dfs(grid, r - 1, c, visit)
        count += self.dfs(grid, r, c - 1, visit)

        visit.remove((r, c))
        return count