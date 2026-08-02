#include <stdbool.h>

/**
 * Predicts if Alice will win the stone game.
 * 
 * @param piles     An array representing the number of stones in each pile.
 * @param pilesSize The total number of piles (guaranteed to be even).
 * @return          true if Alice wins, false otherwise.
 */
bool stoneGame(int* piles, int pilesSize) {
    // Alice always wins by choosing either all odd or all even piles.
    return true;
}
