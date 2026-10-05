class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        # backtracking state: index and curr sum
        def dfs(i: int, curr_sum: int, addends: List[int]):
            # base 1: sum == target
            if curr_sum == target:
                ans.append(addends.copy())
                return
            # base 2: sum > target or index >= length
            if curr_sum > target or i >= len(nums):
                return
            # step 1: choose number at index
            addends.append(nums[i])
            dfs(i, curr_sum + nums[i], addends)
            # step 2: don't choose number at index
            addends.pop()
            dfs(i + 1, curr_sum, addends)
        dfs(0, 0, [])
        return ans

        