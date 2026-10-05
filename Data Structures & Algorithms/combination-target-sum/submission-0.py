class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursion
        add = []
        ans = []
        def dfs(add: List[int], i: int):
            # keep track of nums and index
            # base1: if sum == target add nums and return
            sum_ = sum(add)
            if sum_ == target:
                ans.append(add.copy())
                return
            # base2: if sum > target or index out of bounds return
            elif sum_ > target or i >= len(nums):
                return
            # step: choose current number again
            add.append(nums[i])
            dfs(add, i)
            # step2: skip current number
            add.pop()
            dfs(add, i + 1)
        
        dfs(add, 0)
        return ans
        
           

        