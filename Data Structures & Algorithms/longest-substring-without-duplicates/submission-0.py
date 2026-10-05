class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = right = 0
        maximum = 0
        for char in s:
            while char in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(char)
            maximum = max(maximum, right - left + 1)
            right += 1
        return maximum
