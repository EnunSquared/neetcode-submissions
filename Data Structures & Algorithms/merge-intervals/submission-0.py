class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort list O(nlogn)
        intervals.sort(key = lambda x: x[0])
        curr = intervals[0]
        answer = []
        # loop through list
        for interval in intervals:
            # case 1: curr is before interval
            if curr[1] < interval[0]:
                # append curr
                answer.append(curr)
                # interval is new curr
                curr = interval
            # case 2: curr overlaps
            else:
                # merge interval into curr
                curr[0] = min(curr[0], interval[0])
                curr[1] = max(curr[1], interval[1]) 
        answer.append(curr)
        return answer
        