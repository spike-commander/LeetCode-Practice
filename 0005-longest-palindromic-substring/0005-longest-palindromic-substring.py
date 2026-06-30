class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
        
        start, max_len = 0, 0
        n = len(s)
    
        for i in range(n):
        # Check odd-length palindromes (center at i)
            l1, r1 = i, i
            while l1 >= 0 and r1 < n and s[l1] == s[r1]:
                if (r1 - l1 + 1) > max_len:
                    start = l1
                    max_len = r1 - l1 + 1
                l1 -= 1
                r1 += 1
            
        # Check even-length palindromes (center between i and i+1)
            l2, r2 = i, i + 1
            while l2 >= 0 and r2 < n and s[l2] == s[r2]:
                if (r2 - l2 + 1) > max_len:
                    start = l2
                    max_len = r2 - l2 + 1
                l2 -= 1
                r2 += 1
            
        return s[start:start + max_len]