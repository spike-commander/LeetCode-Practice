from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Array to store the count of set bits (1s) at each bit position
        # Since nums[i] <= 10^9, 30 bits are sufficient (2^30 > 10^9)
        bit_counts = [0] * 32
        
        # Step 1: Count the total frequency of set bits across the entire array
        for num in nums:
            for b in range(32):
                if (num >> b) & 1:
                    bit_counts[b] += 1
        
        # Step 2: Greedily build the k largest possible numbers
        total_sum_squares = 0
        for _ in range(k):
            current_num = 0
            for b in range(32):
                if bit_counts[b] > 0:
                    current_num |= (1 << b)
                    bit_counts[b] -= 1
            
            # Step 3: Add the square of the formed number to the answer
            total_sum_squares = (total_sum_squares + current_num * current_num) % MOD
            
        return total_sum_squares
