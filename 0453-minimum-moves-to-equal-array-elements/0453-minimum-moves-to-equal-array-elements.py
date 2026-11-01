class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # The minimum number of moves is equivalent to 
        # bringing all elements down to the minimum value.
        return sum(nums) - len(nums) * min(nums)
