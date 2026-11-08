class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Track the total number of servers in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        # First pass: Populate the row and column server totals
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        communicating_servers = 0
        
        # Second pass: Count servers that share a row or column with at least one other server
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
