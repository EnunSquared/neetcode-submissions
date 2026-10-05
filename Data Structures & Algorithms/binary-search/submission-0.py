class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #        *        
        # -1, 0, 2, 4, 6, 8               
        #           m     * 
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            if nums[middle] < target:
                left = middle + 1
        return -1
        