import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make negative for max heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        # heapify stones
        heapq.heapify(stones)
        # while theres more than one stone
        while len(stones) > 1:
            # take top two stones and smash them
            heavier = heapq.heappop(stones)
            lighter = heapq.heappop(stones)
            if heavier - lighter < 0:
                heapq.heappush(stones, heavier - lighter)
        if stones:
            return - heapq.heappop(stones)
        else:
            return 0

        