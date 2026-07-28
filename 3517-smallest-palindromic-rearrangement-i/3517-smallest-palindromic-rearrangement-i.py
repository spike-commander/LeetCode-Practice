class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Step 1: Count character frequencies
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        # Step 2: Build the first half and identify the middle character
        mid = ""
        first_half = []
        
        for i in range(26):
            if counts[i] == 0:
                continue
                
            # If frequency is odd, this character belongs in the middle
            if counts[i] % 2 != 0:
                mid = chr(ord('a') + i)
                
            # Add half of the character count to the first half
            first_half.append(chr(ord('a') + i) * (counts[i] // 2))
            
        # Step 3: Combine the first half, center character, and reversed first half
        half_str = "".join(first_half)
        return half_str + mid + half_str[::-1]
