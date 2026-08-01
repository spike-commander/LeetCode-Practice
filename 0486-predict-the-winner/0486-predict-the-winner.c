#include <stdbool.h>

bool predictTheWinner(int* nums, int numsSize) {
    // dp[i][j] stores the maximum relative net score a player can gain from subarray nums[i...j]
    // Constraints state 1 <= numsSize <= 20, so a fixed 20x20 matrix fits perfectly
    int dp[20][20] = {0};
    
    // Base case: If there is only one element in the subarray, the player must pick it
    for (int i = 0; i < numsSize; i++) {
        dp[i][i] = nums[i];
    }
    
    // Build the DP table for subarrays of length 2 up to numsSize
    for (int length = 2; length <= numsSize; length++) {
        for (int i = 0; i <= numsSize - length; i++) {
            int j = i + length - 1;
            
            // Choice 1: Current player picks left element, opponent plays optimally on remaining array
            int pickLeft = nums[i] - dp[i + 1][j];
            
            // Choice 2: Current player picks right element, opponent plays optimally on remaining array
            int pickRight = nums[j] - dp[i][j - 1];
            
            // Maximize the current player's relative score
            dp[i][j] = (pickLeft > pickRight) ? pickLeft : pickRight;
        }
    }
    
    // Player 1 wins if the total relative net score from the full array is >= 0
    return dp[0][numsSize - 1] >= 0;
}
