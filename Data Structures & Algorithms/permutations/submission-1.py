class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # order does matter
        # (n - level) choices at each level in the decision tree
        # O(n!)
        # backtracking where state is current set of permutations
        def dfs(nums_: List[int]) -> List[List[int]]:
            # base case 1: permutations of size 1
            if len(nums_) == 1:
                return [nums_.copy()]
            result = []
            # recursive steps: choosing a specific item in permutations 
            for i in range(len(nums_)):
                # remove an item from list
                item = nums_.pop(0)
                # call permutations on rest of list
                permutations = dfs(nums_)
                # add item + permutations in return result
                for perm in permutations:
                    perm.append(item)
                    result.append(perm)
                nums_.append(item)
            # return list of possible permutations with current set
            return result

        return dfs(nums)
        """
        3 2 1
            2 1 or 1 2
                1
                2
            3 1
            3 2
        """