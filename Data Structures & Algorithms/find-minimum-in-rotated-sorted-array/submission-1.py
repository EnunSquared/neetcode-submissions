class Solution:
    def findMin(self, nums: List[int]) -> int:
        # there is some point where numbers go high-> low
        # check if array has been rotated
        #       if not return first element
        if nums[0] <= nums[-1]:
            return nums[0]
        # do binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            if nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]

        #       success: num > first element
        #       fail: n < first elemnt

        