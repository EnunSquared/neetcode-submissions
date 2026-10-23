class Solution:
    def isValid(self, s: str) -> bool:
        # use hash tables for quick lookup/readability s,t O(1)
        open_lookup = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }
        close_lookup = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []
        #use stack to keep memory of last memory t O(n) s O(n)
        # loop through string
        for char in s:
            # if you see a opening character push to stack
            if char in open_lookup:
                stack.append(char)
            # if you see a closing character pop off stack
            if char in close_lookup:
                # popped off element does not corresponds to closing chark
                if not stack or stack.pop() != close_lookup[char]:
                    return False
        if stack:
            return False
        return True