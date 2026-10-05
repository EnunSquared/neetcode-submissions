import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        #use a max heap to do highest priority tasks
        maxHeap = []
        for i in range(len(count)):
            if count[i] > 0:
                heapq.heappush(maxHeap, (-count[i], i))
        # use a queue with n legnth with dummy values
        queue = deque([(1, -1)] * n)
        ans = 0
        num_tasks = len(tasks)
        print(num_tasks)
        # while heap has elements 
        while num_tasks > 0:
            # pop from heap
            count, letter = heapq.heappop(maxHeap)
            print("curr letter is", letter, "with count", count)
            # increment counter
            ans += 1
            count += 1
            if letter >= 0:
                num_tasks -= 1
            # if more task to be done, append to queue
            if count < 0:
                queue.append((count, letter))
            # else append dummy to queue
            else:
                queue.append((1, -1))
            # add element from front of queue to heap
            heapq.heappush(maxHeap, queue.popleft())
             
        return ans
        