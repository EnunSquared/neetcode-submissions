class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        # sort list t O(nlogn) s O(n) O(1)
        nums.sort()
        # loop through nums O(n)
        for i, num in enumerate(nums):
            # two pointer O(n) to find if set is optional
            l, r = i, len(nums) - 1
            total = -1
            while l < r:
                # skip over self
                if l == i:
                    l += 1
                if r == i:
                    r -= 1
                # if three nums == 0 add to answer
                total = num + nums[l] + nums[r]
                if total == 0:
                    ans.add(tuple(sorted([num, nums[l], nums[r]])))
                    l += 1
                    r -= 1
                # if not increment/decriment left or right depending on if its higher or lower
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return list(ans)
        