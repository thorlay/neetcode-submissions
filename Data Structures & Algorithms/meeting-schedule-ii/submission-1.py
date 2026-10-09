"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start);
        ll = [];
        result = 0;
        for i in intervals:
            left = i.start;
            right = i.end;
            if not ll or ll[0][0] > left:
                result+=1;
                heapq.heappush(ll, [right, left]);
            else:
                heapq.heappop(ll);
                heapq.heappush(ll, [right, left]);
        return result;

            
