import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #can hash counts and iterate through table while keeping track of the k most while popping off a min stack
        counts = defaultdict(int)
        m_heap = []
        heapq.heapify(m_heap)
        # count nums O(n) O(n)
        for num in nums:
            counts[num] += 1
        # loop through items in hash O(n)
        for key, count in counts.items():
            # add item to min heap O(logk)
            heapq.heappush(m_heap, (count, key))
            #if heap > k
            if len(m_heap) > k:
                #pop off top of heap
                heapq.heappop(m_heap)
        # return heap keys
        return [x[1] for x in m_heap]
        
        
        