#include <stdbool.h>
#include <stdlib.h>

/**
 * Predicts if Alice will win the stone game using Dynamic Programming.
 * Works for the general case of the game.
 * 
 * @param piles     An array representing the number of stones in each pile.
 * @param pilesSize The total number of piles.
 * @return          true if Alice wins, false otherwise.
 */
bool stoneGame(int* piles, int pilesSize) {
    // Dynamically allocate a 2D array for the DP table
    int** dp = (int**)malloc(pilesSize * sizeof(int*));
    for (int i = 0; i < pilesSize; i++) {
        dp[i] = (int*)malloc(pilesSize * sizeof(int));
    }

    // Base case: Single piles
    for (int i = 0; i < pilesSize; i++) {
        dp[i][i] = piles[i];
    }

    // Fill the table for subarrays of length 2 to pilesSize
    for (int length = 2; length <= pilesSize; length++) {
        for (int i = 0; i <= pilesSize - length; i++) {
            int j = i + length - 1;
            int pickLeft = piles[i] - dp[i + 1][j];
            int pickRight = piles[j] - dp[i][j - 1];
            
            dp[i][j] = (pickLeft > pickRight) ? pickLeft : pickRight;
        }
    }

    // The result represents Alice's score minus Bob's score
    int netScoreDifference = dp[0][pilesSize - 1];

    // Free allocated memory
    for (int i = 0; i < pilesSize; i++) {
        free(dp[i]);
    }
    free(dp);

    return netScoreDifference > 0;
}
