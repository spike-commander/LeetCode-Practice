class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Find the last occurrence index of each character
        last_idx = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        # Step 2: Iterate through the string to build the result
        for i, char in enumerate(s):
            # Skip characters already included in the active subsequence
            if char in seen:
                continue
            
            # Maintain lexicographical order: pop larger characters 
            # if they appear again later in the string
            while stack and stack[-1] > char and last_idx[stack[-1]] > i:
                seen.remove(stack.pop())
            
            # Add current character to stack and marked as visited
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
