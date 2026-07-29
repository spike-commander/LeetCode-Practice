#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Helper function to calculate unique combinations without causing integer overflow
long long count_permutations(int *half_counts) {
    long long total_perms = 1;
    int total_elements = 0;
    
    for (int i = 0; i < 26; i++) {
        if (half_counts[i] > 0) {
            for (int j = 1; j <= half_counts[i]; j++) {
                total_elements++;
                total_perms = total_perms * total_elements / j;
                
                // Safe boundary check: k <= 10^6, so anything above 2*10^6 is redundant
                if (total_perms > 2000000) {
                    total_perms = 2000000; 
                }
            }
        }
    }
    return total_perms;
}

char* smallestPalindrome(char* s, int k) {
    int len = strlen(s);
    int counts[26] = {0};
    
    // Step 1: Count character frequencies
    for (int i = 0; i < len; i++) {
        counts[s[i] - 'a']++;
    }
    
    char odd_char = '\0';
    int half_counts[26] = {0};
    int total_half_len = 0;
    
    // Step 2: Validate palindrome parity rules and isolate half frequencies
    for (int i = 0; i < 26; i++) {
        if (counts[i] % 2 == 1) {
            if (odd_char != '\0') {
                char* empty = (char*)malloc(1 * sizeof(char));
                empty[0] = '\0';
                return empty; // Fail-safe: Not a valid palindrome layout
            }
            odd_char = 'a' + i;
        }
        half_counts[i] = counts[i] / 2;
        total_half_len += half_counts[i];
    }
    
    // Step 3: Check if k sits outside total valid permutations boundary
    long long total_perms = count_permutations(half_counts);
    if (k > total_perms) {
        char* empty = (char*)malloc(1 * sizeof(char));
        empty[0] = '\0';
        return empty;
    }
    
    // Step 4: Reconstruct the k-th lexicographical half character by character
    char* half_res = (char*)malloc((total_half_len + 1) * sizeof(char));
    int half_idx = 0;
    long long k_remaining = k;
    
    for (int p = 0; p < total_half_len; p++) {
        for (int i = 0; i < 26; i++) {
            if (half_counts[i] > 0) {
                // Try placing the smallest alphabetical character at current index
                half_counts[i]--;
                long long possible_perms = count_permutations(half_counts);
                
                if (k_remaining <= possible_perms) {
                    // The target match sequence lies down this specific branch
                    half_res[half_idx++] = 'a' + i;
                    break;
                } else {
                    // Skip the branch entirely and decrement k by skipped permutations pool
                    k_remaining -= possible_perms;
                    half_counts[i]++; // Backtrack element
                }
            }
        }
    }
    half_res[half_idx] = '\0';
    
    // Step 5: Mirror structural parts into final palindromic string memory block
    char* result = (char*)malloc((len + 1) * sizeof(char));
    int res_idx = 0;
    
    // Copy first half 
    for (int i = 0; i < total_half_len; i++) {
        result[res_idx++] = half_res[i];
    }
    
    // Place middle single element if it exists 
    if (odd_char != '\0') {
        result[res_idx++] = odd_char;
    }
    
    // Mirror the first half elements backwards
    for (int i = total_half_len - 1; i >= 0; i--) {
        result[res_idx++] = half_res[i];
    }
    
    result[res_idx] = '\0';
    
    free(half_res); // Reclaim auxiliary array space
    return result;
}
