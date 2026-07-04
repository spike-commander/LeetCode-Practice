int minScore(int n, int** roads, int roadsSize, int* roadsColSize) {
    // Step 1: Initialize the parent array for Union-Find (1-indexed)
    int* parent = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    
    // Step 2: First Pass - Connect all components
    for (int i = 0; i < roadsSize; i++) {
        int u = roads[i][0];
        int v = roads[i][1];
        
        // Find root of u with iterative Path Compression
        int root_u = u;
        while (root_u != parent[root_u]) {
            root_u = parent[root_u];
        }
        int curr = u;
        while (curr != root_u) {
            int next = parent[curr];
            parent[curr] = root_u;
            curr = next;
        }
        
        // Find root of v with iterative Path Compression
        int root_v = v;
        while (root_v != parent[root_v]) {
            root_v = parent[root_v];
        }
        curr = v;
        while (curr != root_v) {
            int next = parent[curr];
            parent[curr] = root_v;
            curr = next;
        }
        
        // Union step: merge the components
        if (root_u != root_v) {
            parent[root_u] = root_v;
        }
    }
    
    // Step 3: Find the definitive absolute root of City 1
    int root1 = 1;
    while (root1 != parent[root1]) {
        root1 = parent[root1];
    }
    
    // Step 4: Second Pass - Find the minimum edge score in City 1's component
    int min_dist = 10005; // Constraint bound: distance <= 10^4
    for (int i = 0; i < roadsSize; i++) {
        int u = roads[i][0];
        
        // Find root of u using path compression to ensure accurate validation
        int root_u = u;
        while (root_u != parent[root_u]) {
            root_u = parent[root_u];
        }
        
        // If the road belongs to City 1's network, consider its distance
        if (root_u == root1) {
            if (roads[i][2] < min_dist) {
                min_dist = roads[i][2];
            }
        }
    }
    
    // Clean up memory
    free(parent);
    
    return min_dist;
}