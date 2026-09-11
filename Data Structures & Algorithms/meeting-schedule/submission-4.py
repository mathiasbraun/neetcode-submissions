"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intList = []

        for interval in intervals:
            intList.append([interval.start, interval.end])

        intList.sort()

        for i in range(len(intList) - 1):
            if intList[i][1] > intList[i + 1][0]:
                return False
        
        return True