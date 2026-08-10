#include <stdbool.h>
#include <stdlib.h>

bool winnerSquareGame(int n) {
    // Allocate memory for dynamic programming states
    bool* dp = (bool*)malloc((n + 1) * sizeof(bool));
    
    // Base case: 0 stones left means the player whose turn it is loses
    dp[0] = false;
    
    // Compute winning/losing states for all positions up to n
    for (int i = 1; i <= n; i++) {
        dp[i] = false; // Default to losing state
        
        // Check all valid moves (subtracting non-zero perfect squares)
        for (int k = 1; k * k <= i; k++) {
            // If any move leaves the opponent in a losing state, this state is a win
            if (!dp[i - k * k]) {
                dp[i] = true;
                break; // Strategy found, stop checking further squares
            }
        }
    }
    
    bool result = dp[n];
    free(dp); // Prevent memory leak
    return result;
}
