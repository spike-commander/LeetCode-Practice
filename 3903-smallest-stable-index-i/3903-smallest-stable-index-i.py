class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Correctly initialize and precompute suffix minimums
        suff_min = [0] * n
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # Step 2: Traverse from left to right, tracking max on the fly
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            
            # Check instability condition
            if current_max - suff_min[i] <= k:
                return i
                
        return -1
