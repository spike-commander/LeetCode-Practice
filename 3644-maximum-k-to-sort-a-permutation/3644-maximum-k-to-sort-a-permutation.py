from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Initialize max_k to a flag value representing an unset mask
        max_k = -1
        
        for i, val in enumerate(nums):
            # If the element is misplaced, it must participate in a swap
            if val != i:
                if max_k == -1:
                    max_k = val
                else:
                    max_k &= val
                    
        # If max_k remains -1, the array was already sorted
        return max_k if max_k != -1 else 0
