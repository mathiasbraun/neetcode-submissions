import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        
        closest = []
        full = 0

        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            dist = sqrt((xi)**2 + (yi)**2)
            if full < k:
                heapq.heappush(closest, (-dist, points[i]))
                full += 1
            elif dist < -closest[0][0]:
                heapq.heappushpop(closest, (-dist, points[i]))

        return [point for ndist, point in closest]