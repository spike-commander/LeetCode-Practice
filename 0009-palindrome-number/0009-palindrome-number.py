class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if num[::-1] == num:
            return True
        else:
            return False