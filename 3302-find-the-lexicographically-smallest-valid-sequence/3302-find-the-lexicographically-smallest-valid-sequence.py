from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        len1, len2 = len(word1), len(word2)
        
        # last_match[j] will store the largest index in word1 
        # where word1[i] matches word2[j] when matching backwards
        last_match = [-1] * len2
        
        i, j = len1 - 1, len2 - 1
        # Step 1: Precompute the exact match capability from right to left
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last_match[j] = i
                j -= 1
            i -= 1
            
        ans = []
        j = 0
        changed = False # Track if our single character modification has been consumed
        
        # Step 2: Traverse forward to build the lexicographically smallest sequence
        for i in range(len1):
            if j == len2:
                break
                
            # Case A: Natural exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case B: Character mismatch - try using our single modification allowance
            elif not changed:
                # Substitution is valid if:
                # 1. This is the last character of word2 (no remaining suffix constraint)
                # 2. Or the suffix starting at j + 1 can be successfully formed later in word1
                if j == len2 - 1 or i < last_match[j + 1]:
                    ans.append(i)
                    j += 1
                    changed = True
                    
        return ans if len(ans) == len2 else []
