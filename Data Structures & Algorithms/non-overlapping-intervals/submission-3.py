class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort list
        intervals.sort()
        ans = 0
        i = 0
        # loop over every item
        while i < len(intervals) - 1:
            print("start loop at", intervals[i])
            # if end of curr is > start of next
            end = intervals[i][1]
            while i + 1 < len(intervals) and end > intervals[i + 1][0]: 
                print("skipping interval:", intervals[i + 1])
                end = min(end, intervals[i+1][1])
                # increment count
                ans += 1
                # skip next
                i += 1
            i += 1
        return ans
        