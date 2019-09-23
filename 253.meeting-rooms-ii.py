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

# Code by Mincheol
# Runtime: 76 ms, faster than 16.28% of Python online submissions for Meeting Rooms II.
# Memory Usage: 15.3 MB, less than 38.09% of Python online submissions for Meeting Rooms II.

# Algorithm: remove serializable meetings in an iteration. Count how many iteration we have.
class Solution2(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key = lambda P: P[0])

        cnt = 0
        free_list = []
        while len(intervals) > 0:
            free_list.append(intervals[0])
            end = intervals[0][1]
            for i in range(1, len(intervals)):
                if end <= intervals[i][0]:
                    free_list.append(intervals[i])
                    end = intervals[i][1]

            for j in range(len(free_list)):
                intervals.remove(free_list[j])

            free_list = []
            cnt+=1

        return cnt
