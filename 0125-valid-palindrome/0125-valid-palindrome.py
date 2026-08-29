class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        s = s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                n += s[i]
            else:
                continue

        return True if n == n[::-1] else False