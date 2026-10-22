class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # hash with ranges O(n) O(n)
        # hash set then count them O(n) O(n)
        mem = set()
        ans = 0
        for num in nums:
            mem.add(num)
        # count nums in set but only if it is the lowest sequence
        for num in mem:
            if num - 1 not in mem:
                count = 0
                while num + count in mem:
                    count += 1
                ans = max(ans, count)
        return ans

        