import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            maxHeap.append(-num)
        heapq.heapify(maxHeap)
        ans = 0
        for i in range(k):
            ans = -1 * heapq.heappop(maxHeap)
        return ans
        