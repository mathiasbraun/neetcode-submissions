class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set((i, j) for i in range(rows) 
                    for j in range(cols)
                    if grid[i][j] == 1)

        maxArea = 0

        def computeArea(r: int, c: int, visit) -> int:
            if (min(r, c) < 0 or
                    r == rows or c == cols
                    or (r, c) not in visit):
                return 0
            if grid[r][c] == 0:
                return 0
            
            visit.remove((r, c))
            area = 1
            area += computeArea(r + 1, c, visit)
            area += computeArea(r, c + 1, visit)
            area += computeArea(r - 1, c, visit)
            area += computeArea(r, c - 1, visit)

            return area

        while visit:
            pair = next(iter(visit))
            maxArea = max(computeArea(pair[0], pair[1], visit), maxArea)
        
        return maxArea