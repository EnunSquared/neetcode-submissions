class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        l = 0
        min_length = float('inf')
        # len t can be > len s
        # keep a count hashmap
        count = {}
        for char in t:
            count[char] = count.get(char, 0) - 1
        # sliding window
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] = count.get(s[r], 0) + 1
            # if len curr string < len min then update answer
            # contract while all chars in t are acounted for
            print(count)
            print("left", l,"right", r)
            # print("num 0:", list(count.values()).count(0), "length", len(count))
            while all(x >= 0 for x in list(count.values())):
                print("valid string")
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    ans = s[l:r+1]
                if s[l] in count:
                    count[s[l]] -= 1
                l += 1
            # expand iteratively
        return ans
        