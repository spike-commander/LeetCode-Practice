class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        temp = num
        while temp > 0:
            r = temp%10
            if r != 0 and num % r == 0:
                c += 1
            temp//=10
        return c