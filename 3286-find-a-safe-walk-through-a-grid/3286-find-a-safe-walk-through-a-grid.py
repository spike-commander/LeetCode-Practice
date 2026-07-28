from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # Get matrix dimensions
        m, n = len(grid), len(grid[0])
        
        # Array to store the minimum health damage taken to reach each cell
        min_damage = [[float('inf')] * n for _ in range(m)]
        
        # Deque for 0-1 BFS: stores (row, col)
        queue = deque()
        
        # Initialize the starting cell at (0, 0)
        min_damage[0][0] = grid[0][0]
        queue.append((0, 0))
        
        # Direction vectors for moving Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # Check neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Verify within boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Total damage if we step into the neighboring cell
                    next_damage = min_damage[r][c] + grid[nr][nc]
                    
                    # If this path offers fewer health reductions, update and queue it
                    if next_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = next_damage
                        
                        # 0-1 BFS optimization:
                        # Append 0-cost moves to the front, 1-cost moves to the back
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        # Return True if the minimum damage sustained is strictly less than starting health
        return min_damage[m - 1][n - 1] < health
