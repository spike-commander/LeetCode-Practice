class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize the grid entirely with obstacles '#'
        grid = [["#"] * n for _ in range(m)]
        
        # Open the first row completely
        for j in range(n):
            grid[0][j] = "."
            
        # Open the last column completely
        for i in range(m):
            grid[i][n - 1] = "."
            
        # Convert the 2D array of characters into a list of strings
        return ["".join(row) for row in grid]
