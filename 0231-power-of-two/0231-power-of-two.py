class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if (-2)**31 <= n <= 2**31 - 1:
        #    while n%2 == 0:
        #        n//=2
        
        #    return n == 1

        #if (n<=0):
        #    return False
        #if n == 1:
        #    return True
        #if n%2 != 0:
        #    return False
        #return self.isPowerOfTwo(n//2)

        return n > 0 and (n & (n - 1)) == 0