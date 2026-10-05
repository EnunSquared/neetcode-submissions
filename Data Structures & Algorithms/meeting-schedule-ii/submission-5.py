"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals
        intervals.sort(key = lambda x: x.start)
        # keep an array of end times for each day
        day_ends = []
        # loop
        print([(interval.start, interval.end) for interval in intervals])
        for interval in intervals:
            # if next interval starts before theend of all days
            can_fit = False
            for i, end in enumerate(day_ends):
                if interval.start >= end:
                    can_fit = True
                    day_ends[i] = interval.end
                    break
            if not day_ends or not can_fit:
                # append new day end
                day_ends.append(interval.end)
        # return length of days
        print(day_ends)
        return len(day_ends)
        