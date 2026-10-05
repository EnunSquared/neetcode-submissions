class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        for char in t:
            dic[char] -= 1
        print(dic)
        for key in dic:
            if dic[key] != 0:
                return False
        return True
        