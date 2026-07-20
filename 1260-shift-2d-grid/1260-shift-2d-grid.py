class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # 1. Normalize k to avoid redundant full rotations
        k = k % total_elements
        if k == 0:
            return grid
        
        # 2. Flatten the 2D grid into a 1D list
        flat_grid = []
        for row in grid:
            flat_grid.extend(row)
            
        # 3. Rotate the 1D list right by k positions
        # Take the last k elements and place them at the front
        rotated_flat = flat_grid[-k:] + flat_grid[:-k]
        
        # 4. Reshape the 1D list back into the m x n grid
        result = []
        for i in range(0, total_elements, n):
            result.append(rotated_flat[i : i + n])
            
        return result
