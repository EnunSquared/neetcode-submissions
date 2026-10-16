class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        #loop thorugh strings O(n)
        for word in strs:
            # sort string O(klogk)
            # add to hash map O(1) space: O(n)
            mem["".join(sorted(word))].append(word)
        #convert map into list
        return [words for key, words in mem.items()]
        