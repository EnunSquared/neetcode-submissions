class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        # loop through elements
        for num in nums:
            # if element in set return false
            if num in mem:
                return True 
            # else add to set
            mem.add(num)
        return False
        