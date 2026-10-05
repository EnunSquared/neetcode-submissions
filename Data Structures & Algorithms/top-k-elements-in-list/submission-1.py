class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        print(sorted(dic.items(), key = lambda x: x[1]))
        return [x[0] for x in sorted(dic.items(), key = lambda x: x[1])][-k:]
        