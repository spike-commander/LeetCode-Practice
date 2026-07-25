class Solution:
    def maxProduct(self, n: int) -> int:
        # Track the two highest digits found
        max1, max2 = -1, -1
        
        # Process each digit from right to left
        while n > 0:
            digit = n % 10
            n //= 10
            
            # Update the top two largest digits
            if digit > max1:
                max2 = max1
                max1 = digit
            elif digit > max2:
                max2 = digit
                
        return max1 * max2
