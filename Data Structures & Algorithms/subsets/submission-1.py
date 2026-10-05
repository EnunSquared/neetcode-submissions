class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # backtrack where stage is idx
        def helper(i: int, nums_: List[int]): 
            # base case 1: idx === leng
            if i == len(nums):
                ans.append(nums_.copy())
                return
            # recursive step 1: choose item at idx
            nums_.append(nums[i])
            helper(i+1, nums_)
            # recursive step 2: don't choose item at idx
            nums_.pop()
            helper(i +1, nums_)
        helper(0, [])
        return ans
        