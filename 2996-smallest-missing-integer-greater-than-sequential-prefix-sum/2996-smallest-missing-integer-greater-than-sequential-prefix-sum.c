#include <stdio.h>
#include <stdbool.h>

/**
 * Finds the smallest integer x missing from nums such that x is greater than 
 * or equal to the sum of the longest sequential prefix.
 * 
 * Constraints:
 * 1 <= numsSize <= 50
 * 1 <= nums[i] <= 50
 */
int missingInteger(int* nums, int numsSize) {
    // A prefix consisting only of nums[0] is always sequential,
    // so we start with a sum of nums[0].
    int sum = nums[0];
    
    // Find the longest sequential prefix starting from index 1
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + 1) {
            sum += nums[i];
        } else {
            // The sequential prefix breaks here
            break;
        }
    }
    
    // Linear scan to find the smallest missing integer x >= sum
    while (true) {
        bool found = false;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == sum) {
                found = true;
                break;
            }
        }
        
        // If the current sum is not present in the array, 
        // then it is our smallest missing integer.
        if (!found) {
            return sum;
        }
        
        // Otherwise, increment and check the next integer
        sum++;
    }
}
