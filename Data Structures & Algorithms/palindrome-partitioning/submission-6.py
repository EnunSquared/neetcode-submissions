class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #isPalindrome O(n)
        def isPalindrome(start: int, end: int):
            l = start + (end - start)//2
            if (end - start) % 2 == 1:
                r = l + 1
            else:
                r = l
            while l >= start and r <= end:
                if s[l] != s[r]:
                    return False
                l -= 1
                r += 1
            return True
        # potential for memoization
        answer = []
        # dfs where state is index and list of palindromes so far O(n^n)
        def dfs(i: int, palindromes: List[str]):
            # base case 1: index == length of string
            if i == len(s):
                answer.append(palindromes.copy())
                return
            # recursive steps: every possible next palindrome at this index
            for idx in range(i, len(s)):
                if isPalindrome(i, idx):
                    print("Appending string", s[i:idx + 1], "to palindome list", palindromes, "i:", i, "idx", idx)
                    palindromes.append(s[i:idx + 1])
                    dfs(idx + 1, palindromes)
                    palindromes.pop()
        dfs(0, [])
        return answer