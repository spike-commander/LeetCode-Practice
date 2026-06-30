int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    int maxLength = 0;
    int left = 0;
    
    // Array to store the last seen index of each ASCII character
    int lastSeen[128];
    memset(lastSeen, -1, sizeof(lastSeen));
    
    for (int right = 0; right < n; right++) {
        char currentChar = s[right];
        
        // If the character was seen inside the current window, move left pointer
        if (lastSeen[(unsigned char)currentChar] >= left) {
            left = lastSeen[(unsigned char)currentChar] + 1;
        }
        
        // Update the last seen index of the character
        lastSeen[(unsigned char)currentChar] = right;
        
        // Update the maximum length found so far
        maxLength = MAX(maxLength, right - left + 1);
    }
    
    return maxLength;
}