from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case for an array with 1 element
        if n == 1:
            return 1
            
        # Edge case for an array with 2 elements
        if n == 2:
            return 2
            
        # For n >= 3, find the smallest power of 2 strictly greater than n
        ans = 1
        while ans <= n:
            ans *= 2
            
        return ans
