import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put all elements in a hash element -> count O(n) (n space)
        counts = defaultdict(int)
        max_heap = []
        for num in nums:
            counts[num] += 1
        # put all hash key, value pairs into min heap (n*logn) (n)
        for key, count in counts.items():
            heapq.heappush(max_heap, (-count, key))
        # remove k times (logn) (1)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        return ans
        # OR
        # sort elements O(n*logn) (1)
        # loop O(n)
            # hold a counter for each inv char
            # if char is new, check if count is larger than any in counts O(5) O(5)


        