class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        set_ = set()
        for right in range(len(s)):
            # contract when the curr character is in the set
            while s[right] in set_:
                set_.remove(s[left])
                left += 1
            # add char to set and check max length
            print("max", longest, left, right)
            set_.add(s[right])
            longest = max(longest, right - left + 1)
            # expand incrementally
        return longest

'''

'''
