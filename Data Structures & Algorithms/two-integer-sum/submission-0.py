class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash map to store values
        #order the indeces
        bank = {}
        ans = []
        for i, num in enumerate(nums):
            key = target - num
            if key in bank:
                return [min(i,bank[key]), max(i, bank[key])]
            else:
                bank[num] = i
        

        