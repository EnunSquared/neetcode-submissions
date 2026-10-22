class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer t O(n) s O(1)
        l, r = 0, len(s) - 1
        while l < r:
            # check if left, right alphanumeric characer (func)
            # ifnot increment, decriment
            while l< r and not self.isAlphanumeric(s[l]):
                l += 1
            while l<r and  not self.isAlphanumeric(s[r]):
                r -= 1
            # compare left/right
            # make sure capital and lower case are fine
            if s[l].lower() != s[r].lower():
                #return False if not the same
                print(s[l], "is not the same", s[r])
                return False
            l +=1
            r -= 1
        return True

    def isAlphanumeric(self, c: str) -> bool:
        return "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= '9'