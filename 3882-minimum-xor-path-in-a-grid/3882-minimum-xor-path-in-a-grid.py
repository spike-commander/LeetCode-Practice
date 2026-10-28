class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # dp[i][j] stores a set of all possible XOR sums to reach cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case for the starting cell
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                # Skip the starting cell initialization
                if i == 0 and j == 0:
                    continue
                    
                current_val = grid[i][j]
                
                # Check top cell
                if i > 0:
                    for prev_xor in dp[i-1][j]:
                        dp[i][j].add(prev_xor ^ current_val)
                        
                # Check left cell
                if j > 0:
                    for prev_xor in dp[i][j-1]:
                        dp[i][j].add(prev_xor ^ current_val)
        
        # Return the minimum possible XOR value found at the bottom-right cell
        return min(dp[m-1][n-1])
