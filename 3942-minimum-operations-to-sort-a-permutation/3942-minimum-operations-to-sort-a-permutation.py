class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Find the index of the element '0'
        idx0 = nums.index(0)
        
        # Check if the array is circularly increasing
        is_inc = True
        for i in range(n):
            if nums[(idx0 + i) % n] != i:
                is_inc = False
                break
                
        # Check if the array is circularly decreasing
        is_dec = True
        for i in range(n):
            if nums[(idx0 - i + n) % n] != i:
                is_dec = False
                break
                
        # If it fits neither pattern, it's impossible to sort
        if not is_inc and not is_dec:
            return -1
            
        ans = float('inf')
        
        if is_inc:
            # Case A: Pure left rotations -> idx0 steps
            # Case B: Reverse -> Left Rotate -> Reverse -> (n - idx0) + 2 steps
            ans = min(ans, idx0, n - idx0 + 2)
                
        if is_dec:
            # Case C: Reverse first, then left rotate -> n - idx0 steps
            # Case D: Left rotate to n-1 position, then reverse -> idx0 + 2 steps
            ans = min(ans, n - idx0, idx0 + 2)
            
        return ans
