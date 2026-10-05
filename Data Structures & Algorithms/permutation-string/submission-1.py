class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        count = {}
        #hash map of counts of s1
        for char in s1:
            count[char] = count.get(char, 0) - 1
        for i in range(len(s1) - 1):
            count[s2[i]] = count.get(s2[i], 0) + 1
        #fixed sliding window
        for right in range(len(s1) - 1, len(s2)):
            count[s2[right]] = count.get(s2[right], 0) + 1
            # return true if every value in hash is 0
            if list(count.values()).count(0) == len(count):
                return True
            # contract and expand once per loop
            count[s2[left]] -= 1
            left += 1
        return False
        