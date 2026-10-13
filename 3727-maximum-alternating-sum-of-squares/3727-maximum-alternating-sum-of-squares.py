class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Sort elements by their squared values
        nums.sort(key=lambda x: x * x)
        
        n = len(nums)
        mid = n // 2
        
        # Step 2: Sum the smaller half (to be subtracted)
        min_squares_sum = sum(x * x for x in nums[:mid])
        
        # Step 3: Sum the larger half (to be added)
        max_squares_sum = sum(x * x for x in nums[mid:])
        
        # Total maximum score
        return max_squares_sum - min_squares_sum
