class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum exceeds the maximum possible sum for 'num' digits
        if sum > 9 * num:
            # Check if sum is 0 but num > 0, which is invalid since leading zero makes it < num digits
            # However, constraints say 1 <= sum, so sum > 9 * num handles the upper bound.
            return ""
        
        # Calculate the number of 9s and the remainder
        num_9s = sum // 9
        remainder = sum % 9
        
        # Place all 9s first to maximize both value and score
        result = "9" * num_9s
        
        # Append the remainder if it's non-zero
        if remainder > 0:
            result += str(remainder)
            
        # Pad the rest of the digits with 0s to reach exactly 'num' digits
        result += "0" * (num - len(result))
        
        return result
