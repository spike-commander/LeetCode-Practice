class Solution:
    def numberOfSubstrings(self, s: str) -> int:
         # Stores the last seen index of 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
    
        for i, char in enumerate(s):
        # Update the position of the current character
            last_seen[char] = i
        
        # The window is valid if all three characters have been seen at least once
        # The number of valid substrings ending at index i is determined by the 
        # oldest (minimum) index among 'a', 'b', and 'c'.
            count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
        
        return count