#include <stdbool.h>

int uniqueXorTriplets(int* nums, int numsSize) {
    // Step 1: Extract unique elements (S1)
    // Constraints: nums[i] <= 1500, max XOR value < 2048
    bool has_element[1501] = {false};
    int unique_nums[1501];
    int m = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (!has_element[nums[i]]) {
            has_element[nums[i]] = true;
            unique_nums[m++] = nums[i];
        }
    }
    
    // Step 2: Generate all valid pair XOR values (S2)
    // Runs in O(M^2) time where M <= 1500
    bool pair_xor_exists[2048] = {false};
    for (int i = 0; i < m; i++) {
        for (int j = i; j < m; j++) {
            pair_xor_exists[unique_nums[i] ^ unique_nums[j]] = true;
        }
    }
    
    // Step 3: Combine pairs (S2) and unique single elements (S1)
    // Runs in O(2048 * M) time
    bool triplet_xor_exists[2048] = {false};
    int unique_xor_count = 0;
    
    for (int pair_val = 0; pair_val < 2048; pair_val++) {
        if (pair_xor_exists[pair_val]) {
            for (int k = 0; k < m; k++) {
                int triplet_val = pair_val ^ unique_nums[k];
                if (!triplet_xor_exists[triplet_val]) {
                    triplet_xor_exists[triplet_val] = true;
                    unique_xor_count++;
                }
            }
        }
    }
    
    return unique_xor_count;
}
