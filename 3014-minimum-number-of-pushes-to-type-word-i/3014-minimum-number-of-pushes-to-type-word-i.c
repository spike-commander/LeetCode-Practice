#include <string.h>

int minimumPushes(char* word) {
    int n = strlen(word);
    int total_pushes = 0;
    
    // Distribute characters across 8 keys
    for (int i = 0; i < n; i++) {
        total_pushes += (i / 8) + 1;
    }
    
    return total_pushes;
}
