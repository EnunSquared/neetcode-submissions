class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # since there can be duplicates, keep track of tuples
        mem = {}
        ans = []
        # backtrack
        # subset - order doesn't matter
        # keep track of index and num of "includes"
        def dfs(i: int, sub: List[int]) -> List[List[int]]:
            # base case: when n = len of list append list to answer if not in mem
            if i == len(nums):
                key = tuple(sorted(sub))
                if key not in mem:
                    mem[key] = 0
                    ans.append(sub.copy())
                return
            print("i =", i, sub)
            # recusive step 1: choosing current item
            sub.append(nums[i])
            dfs(i + 1, sub)
            sub.pop()
            # recursive step 2: skipping current item 
            dfs(i + 1, sub)
        
        dfs(0, [])
        return ans
            
        