class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # order does not matter
        # sort list in order to group copies together
        candidates.sort()
        ans = []
        # backtracking dfs O(2^n)
        # keeping track of index and sum
        def dfs(i: int, sum_: int, nums: List[int]):
            # base case: target is met
            if sum_ == target:
                # add combination to answer
                ans.append(nums.copy())
                return
            # base case 2: target is exceeded
            if sum_ > target or i >= len(candidates):
                return
            # recursive step 1: include current number
            nums.append(candidates[i])
            dfs(i +1, sum_ + candidates[i], nums)
            # remember to pop off included number before next step
            nums.pop()
            # recursive step 2: don't include number
                # skip repeats of the  current number
            # [2, 1, 1,1, 3]
            #     *  * *   
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            #call recursively
            dfs(i + 1, sum_, nums)

        dfs(0, 0, [])
        return ans
