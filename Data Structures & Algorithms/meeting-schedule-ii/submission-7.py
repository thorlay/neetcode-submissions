"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = 0;
        lasti = [];
        intervals.sort(key = lambda x: x.start);
        for inn in intervals:
            si,ei = inn.start,inn.end;
            if len(lasti) == 0:
                heapq.heappush(lasti, ei)
                n+=1;
                continue;

            if si < lasti[0] :
                n+=1;
                heapq.heappush(lasti, ei)
            elif si >= lasti[0]:
                heapq.heappop(lasti);
                heapq.heappush(lasti, ei)
        return n;


    