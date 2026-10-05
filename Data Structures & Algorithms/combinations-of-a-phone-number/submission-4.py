class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # all possible combinations
        # empty string possible
        # digits between 2 and 9
        # map of digit to strings
        dic = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d','e','f'],
            "4" : ['g','h','i'],
            "5" : ['j','k','l'],
            "6" : ['m','n','o'],
            "7" : ['p','q','r', 's'],
            "8" : ['t','u','v'],
            "9" : ['w','x','y', 'z']
        }
        ans = []
        # backtracking O(3^n)
        # keep track of index
        def dfs(i: int, comb: str):
            # base case index > length
            if i >= len(digits):
                ans.append(comb[:])
                return
            # recursive step: call for each possibility in map
            for letter in dic[digits[i]]:
                #comb += letter
                print("comb before", comb, "i =", i)
                dfs(i + 1, comb + letter)
                #remember to pop off element
                #comb = comb[:-1]
                print("comb after", comb, "i =", i)
        if digits == "":
            return []
        dfs(0, "")
        return ans
        