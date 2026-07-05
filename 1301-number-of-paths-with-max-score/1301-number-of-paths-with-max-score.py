class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[r][c] stores [max_score, path_count]
        # Initialize with [-1, 0] to signify unvisited/unreachable cells
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: start at the bottom-right corner 'S' with 0 score and 1 path
        dp[n-1][n-1] = [0, 1]
        
        # Traverse the board backwards from bottom-right to top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip if current cell is an obstacle or is unreachable
                if board[r][c] == 'X' or dp[r][c][0] == -1:
                    continue
                    
                current_score, current_count = dp[r][c]
                
                # Permitted moves moving backward: Up, Left, and Up-Left
                directions = [(r - 1, c), (r, c - 1), (r - 1, c - 1)]
                
                for nr, nc in directions:
                    # Check grid boundaries and obstacles
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':
                        # 'E' adds 0 to score, otherwise extract the numeric digit
                        cell_value = int(board[nr][nc]) if board[nr][nc].isdigit() else 0
                        next_score = current_score + cell_value
                        
                        # Found a higher score path to (nr, nc)
                        if next_score > dp[nr][nc][0]:
                            dp[nr][nc] = [next_score, current_count]
                        # Found an alternative path yielding the exact same max score
                        elif next_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + current_count) % MOD

    # Extract results from the destination top-left cell 'E'
        final_score, final_count = dp[0][0]
    
    # If destination was never reached, return [0, 0]
        return [final_score, final_count] if final_score != -1 else [0, 0]
