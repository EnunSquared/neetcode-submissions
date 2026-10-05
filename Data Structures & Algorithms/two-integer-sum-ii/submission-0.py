class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hash map O(n) time O(n) space
        # two pointer solution O(n) time O(1) space
        left = 0
        right = len(numbers) - 1
        # while l < r
        while left < right:
            # if l + r == target
            if numbers[left] + numbers[right] == target:
                # 1 - indexed
                return [left + 1, right + 1]
            # if l + r < target
            if numbers[left] + numbers[right] < target:
                # l += 1
                left += 1
            # if l + r > target
            if numbers[left] + numbers[right] > target:
                #  r -= 1
                right -= 1
        return []
        