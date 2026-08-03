#include <string.h>
#include <limits.h>

char* stoneGameIII(int* stoneValue, int stoneValueSize) {
    // Array to hold the DP values for the next 3 positions plus a boundary
    int dp[4] = {0, 0, 0, 0};

    // Iterate backwards from the last stone to the first stone
    for (int i = stoneValueSize - 1; i >= 0; i--) {
        int current_take = 0;
        int max_advantage = INT_MIN;

        // Try taking 1, 2, or 3 stones
        for (int k = 0; k < 3 && i + k < stoneValueSize; k++) {
            current_take += stoneValue[i + k];
            // The index in our circular/shifted DP array
            int next_dp_val = dp[(i + k + 1) % 4]; 
            int current_advantage = current_take - next_dp_val;
            
            if (current_advantage > max_advantage) {
                max_advantage = current_advantage;
            }
        }
        // Store the result for the current index i
        dp[i % 4] = max_advantage;
    }

    // Alice's final maximum score advantage starting from index 0
    int alice_advantage = dp[0];

    if (alice_advantage > 0) {
        return "Alice";
    } else if (alice_advantage < 0) {
        return "Bob";
    } else {
        return "Tie";
    }
}
