class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = []
        # make a list of string lengths O(n) O(n)
        for word in strs:
            lens.append(str(len(word)))
        # add the lengths of string seperated by a '#'
        # return string of string lengths, '#', then letters
        return "#".join([",".join(lens), "".join(strs)])

    def decode(self, s: str) -> List[str]:
        # get list of string lengths from string O(n) O(n)
        print(s)
        i = 0
        lens = []
        # make a list of strings based of lengths
        while s[i] != '#':
            start = i
            while s[i] != ',' and s[i] != '#':
                print(s[i])
                i += 1
            lens.append(int(s[start:i]))
            if s[i] != '#':
                i += 1
        # loop through string
        i = i + 1
        ans = []
        j = 0
        for l in lens:
            # splice string using string length
            # add to list
            ans.append(s[i:i+l])
            # iterate by string length
            i += l
        return ans
