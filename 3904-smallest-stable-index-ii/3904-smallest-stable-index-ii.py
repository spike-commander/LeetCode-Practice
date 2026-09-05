class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        # Step 1: Precompute suffix minimums
        suff_min = [0] * n
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # Step 2: Track prefix maximum dynamically and find the first stable index
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            
            # Instability score calculation
            if current_max - suff_min[i] <= k:
                return i
                
        return -1
