class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if len(intervals) == 1:
            return intervals
        
        res = [[intervals[0][0], intervals[0][1]]]
        l, r = 0, 1
        i = 0

        while r < len(intervals):
            if intervals[r][0] <= res[i][1]:
                res[i] = [res[i][0], max(res[i][1], intervals[r][1])]
                r += 1
            else:
                res.append([intervals[r][0], intervals[r][1]])
                l = r
                r = l + 1
                i += 1

        return res