class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted so we can guarentee that moving in certain direction increases/decreases calues
        #start pointer at either end
        left = 0
        right = len(numbers) - 1
        total = numbers[left] + numbers[right]
        while total != target:
            total = numbers[left] + numbers[right]
            #print(left, right, total)
            # if sum is lower,  increment left pinter
            if total < target:
                left += 1
            # if sum is higher,decrease right pointer
            if total > target:
                right -= 1
        return [left + 1, right + 1]
        