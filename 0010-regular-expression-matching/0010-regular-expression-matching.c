bool isMatch(char* s, char* p) {
    int s_len = 0;
    while (s[s_len]) s_len++;
    
    int p_len = 0;
    while (p[p_len]) p_len++;
    
    // Allocate DP table with size (s_len + 1) x (p_len + 1)
    bool dp[s_len + 1][p_len + 1];
    
    // Explicitly initialize the array to false
    for (int i = 0; i <= s_len; i++) {
        for (int j = 0; j <= p_len; j++) {
            dp[i][j] = false;
        }
    }
    
    // Base case: empty string matches empty pattern
    dp[0][0] = true;
    
    // Initialize first row for patterns like a*, a*b*, .* that match empty string
    for (int j = 1; j <= p_len; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 2];
        }
    }
    
    // Fill the remaining entries of the table
    for (int i = 1; i <= s_len; i++) {
        for (int j = 1; j <= p_len; j++) {
            // Case 1: Exact character match or '.' wildcard
            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } 
            // Case 2: '*' wildcard
            else if (p[j - 1] == '*') {
                // Subcase A: Match 0 instances of the preceding character
                dp[i][j] = dp[i][j - 2];
                
                // Subcase B: Match 1 or more instances if preceding character fits
                if (p[j - 2] == s[i - 1] || p[j - 2] == '.') {
                    dp[i][j] = dp[i][j] || dp[i - 1][j];
                }
            }
        }
    }
    
    return dp[s_len][p_len];
}
