class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = "".join(i.lower() for i in s if i.isalnum())
        result = si == si[::-1]
        return result