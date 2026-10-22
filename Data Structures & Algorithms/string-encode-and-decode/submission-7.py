class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        # loop through strings O(n)
        for word in strs:
            #add len of string to list with symbol at end space O(n)
            code.append(str(len(word)))
            code.append('#')
            #add string to list space O(n)
            code.append(word)
        # return string to list
        return "".join(code)

    def decode(self, s: str) -> List[str]:
        ans = []
        #loop through string O(n)
        i = 0
        while i < len(s):
            # get number (loop until #)
            start = i
            while s[i] != '#':
                i += 1
            size = int(s[start:i])
            i += 1
            # splice word using number
            # add number to list
            ans.append(s[i:i +size])
            i += size
        # return ans
        return ans
