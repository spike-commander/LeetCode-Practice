class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If t is longer than s, it cannot be a subsequence
        if m < n:
            return 0
            
        # Space-optimized DP array
        # dp[j] stores the count of subsequences matching t[0...j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: An empty string t has 1 match (deleting all chars of s)

        for i in range(1, m + 1):
            # Traverse backwards to safely overwrite the current DP layer
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]
