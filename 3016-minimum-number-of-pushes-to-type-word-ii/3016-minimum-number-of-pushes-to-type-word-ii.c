#include <string.h>
#include <stdlib.h>

// Helper comparator function to sort integers in descending order
int compareDescending(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int minimumPushes(char* word) {
    // Array to store the frequency of each letter from 'a' to 'z'
    int frequencies[26] = {0};
    
    // Count the frequency of each character in the string
    for (int i = 0; word[i] != '\0'; i++) {
        frequencies[word[i] - 'a']++;
    }
    
    // Sort frequencies in descending order to prioritize most frequent letters
    qsort(frequencies, 26, sizeof(int), compareDescending);
    
    int totalPushes = 0;
    
    // Calculate total pushes based on greedy placement (8 keys available: 2 to 9)
    for (int i = 0; i < 26 && frequencies[i] > 0; i++) {
        // First 8 letters take 1 push, next 8 take 2 pushes, and so on.
        int costPerPush = (i / 8) + 1; 
        totalPushes += frequencies[i] * costPerPush;
    }
    
    return totalPushes;
}
