class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(nlogn)
        candidates.sort()
        # keep a set of added lists
        ans = []
        mem = set()

        # backtracking where index, subset, and sum is the state O(2^n)
        def backtrack(i: int, subset: List[int], target: int):
            print("index:", i, "set:", subset, "target", target)
            # base case 2: target == 0
            if target == 0 and tuple(subset) not in mem:
                ans.append(subset.copy())
                mem.add(tuple(subset))
                return
            # base case 1: out of bounds or target < 0 or subset in list
            if i >= len(candidates) or target < 0 or tuple(subset) in mem:
                return
            # recursive step 1: choose current number
            subset.append(candidates[i])
            backtrack(i + 1, subset, target - candidates[i])
            # step 2: don't choos current number
            subset.pop()
            backtrack(i + 1, subset, target)

        backtrack(0, [], target)
        return ans