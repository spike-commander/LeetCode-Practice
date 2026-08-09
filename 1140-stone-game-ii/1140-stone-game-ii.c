#include <string.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int stoneGameII(int* piles, int pilesSize) {
    int n = pilesSize;
    
    // suffix_sums[i] stores the sum of piles from index i to n-1
    int suffix_sums[n + 1];
    memset(suffix_sums, 0, sizeof(suffix_sums));
    for (int i = n - 1; i >= 0; i--) {
        suffix_sums[i] = suffix_sums[i + 1] + piles[i];
    }
    
    // dp[i][m] table
    // Since X can be up to 2M, and M can grow up to N, M is bounded by N
    int dp[n + 1][n + 1];
    memset(dp, 0, sizeof(dp));
    
    // Populate DP table from right to left
    for (int i = n - 1; i >= 0; i--) {
        for (int m = 1; m <= n; m++) {
            // Base case: If the player can take all remaining piles
            if (i + 2 * m >= n) {
                dp[i][m] = suffix_sums[i];
                continue;
            }
            
            // Try taking X piles, where 1 <= X <= 2M
            int max_stones = 0;
            for (int x = 1; x <= 2 * m; x++) {
                int next_m = MAX(m, x);
                // Your stones = total remaining stones - optimal stones opponent can get next turn
                int current_stones = suffix_sums[i] - dp[i + x][next_m];
                max_stones = MAX(max_stones, current_stones);
            }
            dp[i][m] = max_stones;
        }
    }
    
    // The game starts at pile 0 with M = 1
    return dp[0][1];
}
