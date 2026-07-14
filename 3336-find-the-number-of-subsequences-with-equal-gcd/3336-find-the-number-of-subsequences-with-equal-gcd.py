import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the number of valid pairs with GCDs g1 and g2
        dp = {}
        dp[(0, 0)] = 1  # Base case: both subsequences are empty
        
        for x in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Choice 1: Add x to seq1
                ng1 = math.gcd(g1, x) if g1 != 0 else x
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                # Choice 2: Add x to seq2
                ng2 = math.gcd(g2, x) if g2 != 0 else x
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
            dp = next_dp
            
        # Sum up all states where g1 == g2 and both subsequences are non-empty (> 0)
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans
