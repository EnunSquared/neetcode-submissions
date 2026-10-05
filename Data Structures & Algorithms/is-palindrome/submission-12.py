class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s.lower():
            if (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                string += char
        # start pointers in middle
        left = math.floor(len(string) / 2)
        if len(string) % 2 == 0:
            left -= 1
        right = left + 1 if len(string) % 2 == 0 else left
        print(string, len(string))
        print(left, right)
        # move pointers while checking if equal
        while left >= 0 and right < len(string):
            print(left, right)
            if string[left] != string[right]:
                return False
            left -= 1
            right += 1
        return True
        