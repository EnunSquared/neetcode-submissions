class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: loop through all solutions and sort them into buckets by comparing them individually
        # use hash with string since max num of char is 100 O()
        #use hash map tuple -> list
        ans = defaultdict(list)
        # loop thorugh list
        for word in strs:
            count = [0] * 26
            # for each word make a tuple of all the chars
            for char in word:
                count[ord(char) - ord('a')] += 1
            #append it to list at tuple
            ans[tuple(count)].append(word)
        return list(ans.values())
        