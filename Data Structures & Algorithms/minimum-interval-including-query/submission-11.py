import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals O(nlogn)
        intervals.sort(key = lambda x : x[0])
        # sort queries O(klogk) while keeping original position
        sorted_qs = sorted(enumerate(queries), key = lambda q: q[1])
        ans = [-1] * len(queries)
        minheap = []
        # for every query
        curr = 0
        for i, query in sorted_qs:
            # while curr interval start <= query and end >= query
            while curr < len(intervals) and query >= intervals[curr][0]:
                length = intervals[curr][1] - intervals[curr][0] + 1
                # add to minheap O(logn)
                heapq.heappush(minheap, (length, intervals[curr][1]))
                curr += 1
            # while top of minheap doesn't include query
            while minheap and minheap[0][1] < query:
                # pop from minhead O(logn)
                heapq.heappop(minheap)
            # append top of minheap to answer if not empty else -1
            ans[i] = minheap[0][0] if minheap else -1
        return ans 