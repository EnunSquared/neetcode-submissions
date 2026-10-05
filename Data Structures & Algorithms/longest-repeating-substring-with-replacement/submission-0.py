class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        char_bank = {}
        most_freq = 0
        # sliding window
        for right in range(len(s)):
            # X Y Y X
            # *               
            #       *        
            # most_freq:2  longest:4
            # bank: 
            #            X:2 
            #            Y:2
            #             : 
            
            #print("left",left,"right",right)
            #print( "lengt", right - left + 1, "minus", most_freq)
            # add new char and keep track of char with max frequency
            char_bank[s[right]] = char_bank.get(s[right], 0) + 1
            most_freq = max(char_bank[s[right]], most_freq)

            #contract while the amount of chars needing replacement is < k
            while (right - left + 1) - most_freq > k:
                char_bank[s[left]] -= 1
                left += 1
            
            
            # check to see if length of curr subarray is new longest
            print("left",left,"right",right)
            print("longest was", longest, "checking", right - left + 1)
            longest = max(longest, right - left + 1)
            # expand incrementally
        return longest
        