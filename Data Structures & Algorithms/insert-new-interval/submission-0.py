class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval
        result = []
        i, n = 0, len(intervals)

        # Intervals entirely left of the new one (end before a)
        while i < n and intervals[i][1] < a:
            result.append(intervals[i])
            i += 1

        # Intervals overlapping the new one (start at most b): merge them into [a, b]
        while i < n and intervals[i][0] <= b:
            a = min(a, intervals[i][0])
            b = max(b, intervals[i][1])
            i += 1
        result.append([a, b])

        # Intervals entirely right of the new one
        result.extend(intervals[i:])
        return result