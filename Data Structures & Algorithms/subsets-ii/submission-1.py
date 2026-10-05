class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # each level produces an answer -> answer not returned by dfs
        # since there are duplicates number we need to sort O(nlogn)
        #  1, 1, 2
        #  .  .
        #        .
        # O (2^n)
        # dfs where state is index and subset so far
        nums.sort()

        def dfs(i: int, subset: List[int]) -> List[List[int]]:
            # base case: if index > length
            if i >= len(nums):
                return [subset.copy()]
            # recursive step 1: choose to include curr number
            subset.append(nums[i])
            ans = dfs(i + 1, subset)
            # recursive step 2: choose to skip curr number
            subset.pop()
            i += 1
            # when making the choice not to include a number skip to the end
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            # return combination of lists
            ans.extend(dfs(i, subset))
            return ans

        answer = dfs(0, [])
        return answer
        