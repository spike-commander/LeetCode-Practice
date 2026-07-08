class Solution:
    def myPow(self, x: float, n: int) -> float:
        if -100 < x < 100 or (-2)**31 <= n <= 2**31:
            if n == 0:
                return 1
            if n == 1:
                return x
            return x**n