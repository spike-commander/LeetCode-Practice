from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # Using a generator expression to sum up the squares of special elements
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)
