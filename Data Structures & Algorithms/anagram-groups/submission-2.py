class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(num_chars: List[int]):
            hash = ""
            for i, num in enumerate(num_chars):
                if num > 0:
                    hash += chr(num) + chr(i + 97)
            return hash

        table = collections.defaultdict(list)
        for string in strs:
            chars = [0] * 26    
            # count num of letters in string O(s)
            for char in string:
                chars[ord(char) - 97] += 1
            # hash numbers O(26) -> O(1)
            hash_ = hash(chars)
            print("hash", hash_, "for string", string)
            # append string to table at hash
            table[hash_].append(string)
        return table.values()
            