class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits are num 2-9
        # array arrays of strings
        numToChar = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]
        # potential memory optimization
        # dfs state is index 
        answer = []
        def dfs(i: int, string: str) -> List[str]:
            # base case 1: i == length of digits
            if i == len(digits):
                if string:
                    answer.append(string)
                return
            # recursive steps: choose each number for number at index 
            for char in numToChar[int(digits[i])]:
                dfs(i + 1, string + char)
        dfs(0, "")
        return answer