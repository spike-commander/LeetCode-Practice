from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        divisible_islands = 0
        
        # Directions for 4-directional movement: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(rows):
            for c in range(cols):
                # If we find a positive integer, it's a new island
                if grid[r][c] > 0:
                    island_sum = 0
                    queue = deque([(r, c)])
                    
                    # Accumulate value and mark the starting cell as visited (0)
                    island_sum += grid[r][c]
                    grid[r][c] = 0
                    
                    # Standard BFS traversal to explore the entire island
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Check boundaries and if the neighbor is valid land
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                    
                    # Check if the island's total value is divisible by k
                    if island_sum % k == 0:
                        divisible_islands += 1
                        
        return divisible_islands
