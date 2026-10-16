import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count elements with hash table O(n) O(n)
        mem = defaultdict(int)
        max_heap = []
        heapq.heapify(max_heap)
        ans = []
        for num in nums:
            mem[num] += 1
        # sort them by most frequenst
        # loop hash table  
        for num, count in mem.items():
            #add to max heap
            heapq.heappush(max_heap, (-count, num))
        # pop off k elements
        for i in range(k):
            num = heapq.heappop(max_heap)[1]
            ans.append(num)
        return ans
        