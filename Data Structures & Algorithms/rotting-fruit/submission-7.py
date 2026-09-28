from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = [(i, j) for i in range(rows) for j in range(cols) 
                    if grid[i][j] == 2]
        q = deque(rotten)
        visit = set(rotten)

        fresh = set((i, j) for i in range(rows) for j in range(cols) 
                    if grid[i][j] == 1)

        if not fresh:
            return 0

        minutes = 0
        while q:
            k = len(q)
            for i in range(k):
                r, c = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in dirs:
                    if (min(r + dr, c + dc) < 0 
                        or r + dr == rows or c + dc == cols
                        or (r + dr, c + dc) in visit 
                        or grid[r + dr][c + dc] == 0):
                        continue
                    if grid[r + dr][c + dc] == 1:
                        q.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                        fresh.remove((r + dr, c + dc))
            minutes += 1
            if not fresh:
                return minutes

        return -1
