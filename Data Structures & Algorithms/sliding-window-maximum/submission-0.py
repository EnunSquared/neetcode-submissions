class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        l = 0
        ans = []
        #fixed sliding window
        for r in range(len(nums)):
            # monotonic stack to keep track of top values
            # can sue 
            print(stack)
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
            #if nums[stack[-1]] < nums[r]:
            stack.append(r)
            
            if r >= k - 1:
                ans.append(nums[stack[0]])
                l += 1
            # use indexes to keep track of what to remove from end of stck 
            if r >= k - 1 and stack[0] < l:
                stack.popleft()
            # iterave contracting and expanding
        return ans
        