class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #order matters
        # base case is length of 1
        if len(nums) == 1:
            print(nums)
            print(nums[:])
            return [nums.copy()]
        ans = []
        # recursion 
        # loop through list of nums to get all permutations
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
            ans.extend(perms)
            nums.append(num)
        return ans
        
        