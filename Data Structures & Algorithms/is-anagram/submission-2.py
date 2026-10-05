class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hash map
        mem = {}
        # if strings unequal size return false
        if len(s) != len(t):
            return False
        #loop through string
        for char in s:
            #if letter in map
            if char in mem:
                #increase count by 1
                mem[char] += 1
            #if not in map
            else:
            # add letters to map with count 1
                mem[char] = 1
        # loop trough t
        for char in t:
            # if letter not in map
            if char not in mem:
                return False
            # lower count
            mem[char] -= 1
            #if count < 0
            if mem[char] < 0:
                #return false
                return False
        return True
        