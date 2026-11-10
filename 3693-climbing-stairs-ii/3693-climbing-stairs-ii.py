class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # Starting point cost is 0
        
        for i in range(1, n + 1):
            # Check jumping from i-1
            if i - 1 >= 0:
                dp[i] = min(dp[i], dp[i-1] + costs[i-1] + 1) # 1^2 = 1
            # Check jumping from i-2
            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i-2] + costs[i-1] + 4) # 2^2 = 4
            # Check jumping from i-3
            if i - 3 >= 0:
                dp[i] = min(dp[i], dp[i-3] + costs[i-1] + 9) # 3^2 = 9
                
        return dp[n]
