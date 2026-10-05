class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        maximum = 0
        #hash numbers with range pairs
        for num in nums:
            # start range of itself
            upper = num
            lower = num
            if num not in dic:
                dic[num] = (upper, lower)
                #both upper and lower exist
                if num + 1 in dic and num - 1 in dic:
                    upper = dic[num+1][1]
                    lower = dic[num-1][0]
                    dic[upper] = (lower, upper)
                    dic[lower] = (lower, upper)
                # update lower number if they exist
                elif num + 1 in dic:
                    upper = dic[num+1][1]
                    dic[num] = (lower, upper)
                    dic[upper] = (lower, upper)
                # update upper number if they exist
                elif num - 1 in dic:
                    lower = dic[num-1][0]
                    dic[num] = (lower, upper)
                    dic[lower] = (lower, upper)
            # update edges of max adjacent
            maximum = max(maximum, upper - lower + 1)
        return maximum
                
        