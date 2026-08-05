#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* remainingMethods(int n, int k, int** invocations, int invocationsSize, int* invocationsColSize, int* returnSize) {
    // Step 1: Build the adjacency list for the invocation graph
    int* head = (int*)malloc(n * sizeof(int));
    int* next = (int*)malloc(invocationsSize * sizeof(int));
    int* to = (int*)malloc(invocationsSize * sizeof(int));
    
    for (int i = 0; i < n; i++) {
        head[i] = -1;
    }
    
    for (int i = 0; i < invocationsSize; i++) {
        int u = invocations[i][0];
        int v = invocations[i][1];
        to[i] = v;
        next[i] = head[u];
        head[u] = i;
    }

    // Step 2: Mark all suspicious methods reachable from k using BFS
    bool* suspicious = (bool*)calloc(n, sizeof(bool));
    int* queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;

    queue[rear++] = k;
    suspicious[k] = true;

    while (front < rear) {
        int curr = queue[front++];
        for (int e = head[curr]; e != -1; e = next[e]) {
            int neighbor = to[e];
            if (!suspicious[neighbor]) {
                suspicious[neighbor] = true;
                queue[rear++] = neighbor;
            }
        }
    }

    // Step 3: Check if any external method invokes a suspicious method
    bool canRemove = true;
    for (int i = 0; i < invocationsSize; i++) {
        int u = invocations[i][0];
        int v = invocations[i][1];
        // If an external method (not suspicious) invokes a suspicious method
        if (!suspicious[u] && suspicious[v]) {
            canRemove = false;
            break;
        }
    }

    // Step 4: Construct the result array based on validity
    int* result = NULL;
    if (!canRemove) {
        // Cannot remove anything; return all methods
        *returnSize = n;
        result = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            result[i] = i;
        }
    } else {
        // Count remaining non-suspicious methods
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) count++;
        }
        
        *returnSize = count;
        result = (int*)malloc(count * sizeof(int));
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) {
                result[idx++] = i;
            }
        }
    }

    // Clean up allocated memory helper arrays
    free(head);
    free(next);
    free(to);
    free(suspicious);
    free(queue);

    return result;
}
