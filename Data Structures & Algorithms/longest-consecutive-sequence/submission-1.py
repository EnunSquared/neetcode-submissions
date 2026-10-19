class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash with ranges
        mem = {}
        ans = 0
        # for num in nums O(n)
        for num in nums:
            # check lowest
            if num not in mem:
                # if no number lower self is lowest
                # if there is number higher self is higst
                lowest = highest = num
                # if there is a numer lower update lowest's highest and self's lowest
                if num - 1 in mem:
                    lowest = mem[num-1][0]
                # check highest
                # else update self highest and highests' lowest
                if num + 1 in mem:
                    highest = mem[num+1][1]
                mem[lowest] = (lowest, highest)
                mem[highest] = (lowest, highest)
                ans = max(ans, highest-lowest + 1)
                
        return ans
        