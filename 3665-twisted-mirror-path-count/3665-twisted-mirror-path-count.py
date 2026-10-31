from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Base case: if start or end is blocked, no paths exist
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0
            
        # to_down[i][j] stores the final empty cell reached if a robot 
        # enters mirror (i, j) while moving RIGHT (which reflects it DOWN)
        to_down = [[None] * n for _ in range(m)]
        # to_right[i][j] stores the final empty cell reached if a robot 
        # enters mirror (i, j) while moving DOWN (which reflects it RIGHT)
        to_right = [[None] * n for _ in range(m)]
        
        # Step 1: Precalculate mirror reflection paths from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    # Case A: Entered moving RIGHT -> turned DOWN to (i + 1, j)
                    if i + 1 < m:
                        if grid[i + 1][j] == 0:
                            to_down[i][j] = (i + 1, j)
                        else:
                            to_down[i][j] = to_right[i + 1][j]
                            
                    # Case B: Entered moving DOWN -> turned RIGHT to (i, j + 1)
                    if j + 1 < n:
                        if grid[i][j + 1] == 0:
                            to_right[i][j] = (i, j + 1)
                        else:
                            to_right[i][j] = to_down[i][j + 1]
        
        # Step 2: Main DP table for empty cells
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1 # Destination base case
        
        # Process cells from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Mirrors don't hold individual choices; we skip them
                if grid[i][j] == 1 or (i == m - 1 and j == n - 1):
                    continue
                
                paths = 0
                
                # Option 1: Move Right
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        paths += dp[i][j + 1]
                    else:
                        dest = to_down[i][j + 1]
                        if dest:
                            paths += dp[dest[0]][dest[1]]
                            
                # Option 2: Move Down
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        paths += dp[i + 1][j]
                    else:
                        dest = to_right[i + 1][j]
                        if dest:
                            paths += dp[dest[0]][dest[1]]
                
                dp[i][j] = paths % MOD
                
        return dp[0][0]
