"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
            
        # Sort by how early they start. You want two data structures here.
        intervals.sort(key=lambda x: x.start, reverse=False)
        
        # Next, we create a heap and put the first element's end time. We want a min heap:
        rooms = []
        rooms.append(intervals[0].end)
        
        # Funny thing about the heapq api is that heapq always stores a min-heap. If you want a maxheap,
        # negate your values first, all multiply by -1. SO the larger the value is, the smaller it is when negated.
        # Fortunately we only need a min-heap here. Iterate over all meetings, and add to the heap. Pop if it replaces an
        # existing meeting.
        
        for meeting_no in range(1, len(intervals)):
            meeting = intervals[meeting_no]
            
            if meeting.start < rooms[0]:
                heapq.heappush(rooms, meeting.end)
            else:
                heapq.heappushpop(rooms, meeting.end)
                
        
        return len(rooms)
