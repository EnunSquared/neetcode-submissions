import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            point = points[i]
            dist = point[0] ** 2 + point[1] ** 2
            if i < k:
                heapq.heappush(heap, (-dist, point)) 
            elif -dist > heap[0][0]:
                print("removing point", heap[0][1], "dist",heap[0][0],
                        "for point", point, "dist", -dist)
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, point))
        return [x[1] for x in heap]
                
        