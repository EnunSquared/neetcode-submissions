class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer O(n) O(1)
        # start at ends to have maximum width
        left =  0
        right = len(heights) - 1
        ans = (right - left) * min(heights[left], heights[right])
        while left < right:
            # decriment one side depending on which lowers has the highest hight
            ans = max(ans, (right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            # compare to max
            #print(heights[left], heights[right] , (right - left) * min(heights[left], heights[right]))
        return ans
        
        