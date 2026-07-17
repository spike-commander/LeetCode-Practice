from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # 1. Count frequency of each number in nums
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        # 2. Count how many elements are multiples of each index i
        multiples_count = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                multiples_count[i] += counts[j]
                
        # 3. Calculate exact number of pairs having GCD equal to i
        gcd_pairs_count = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            cnt = multiples_count[i]
            total_pairs = cnt * (cnt - 1) // 2
            
            # Subtract pairs that have a larger common multiple of i
            minus = 0
            for j in range(2 * i, max_val + 1, i):
                minus += gcd_pairs_count[j]
                
            gcd_pairs_count[i] = total_pairs - minus
            
        # 4. Build prefix sums of GCD pair frequencies
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_pairs_count[i]
            
        # 5. Map queries to their respective GCD values via binary search
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
