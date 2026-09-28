from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        if rows == 1 and cols == 1:
            return 0

        q = deque([(0, 0)])
        visit = set([(0, 0)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == rows or c + dc == cols or
                        (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == 1):
                        continue
                    if r + dr == rows - 1 and c + dc == cols - 1:
                        return length
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1    
