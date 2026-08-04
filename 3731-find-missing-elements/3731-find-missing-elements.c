#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingElements(int* nums, int numsSize, int* returnSize) {
    int min = nums[0];
    int max = nums[0];
    
    // 1. Find the min and max elements to define the original range
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < min) min = nums[i];
        if (nums[i] > max) max = nums[i];
    }
    
    // 2. Track the presence of each number using a lookup array
    // Constraints state 1 <= nums[i] <= 100, so size 101 is safe
    int present[101] = {0};
    for (int i = 0; i < numsSize; i++) {
        present[nums[i]] = 1;
    }
    
    // 3. Count how many numbers are missing
    int expectedTotal = max - min + 1;
    int missingCount = expectedTotal - numsSize;
    
    // 4. Handle the case where no numbers are missing
    if (missingCount <= 0) {
        *returnSize = 0;
        return NULL;
    }
    
    // 5. Allocate memory and populate with missing elements in sorted order
    int* missingNumbers = (int*)malloc(missingCount * sizeof(int));
    int index = 0;
    
    for (int i = min; i <= max; i++) {
        if (!present[i]) {
            missingNumbers[index++] = i;
        }
    }
    
    *returnSize = missingCount;
    return missingNumbers;
}
