class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two arrays time O(n) space O(n)
        left_to_right = [1] * len(nums)
        right_to_left = [1] * len(nums)
        # left to right products # O(n)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            left_to_right[i] = product
        # right to left products
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            right_to_left[i] = product
        # find result by using products
        # multiply left to right and right to left at index in answer array
        return [x*y for x, y in zip(left_to_right, right_to_left)]