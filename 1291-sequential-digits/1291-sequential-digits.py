class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        # Loop through all possible lengths of numbers (from 2 digits up to 9 digits)
        for length in range(2, 10):
            # Slide the window across the 'digits' string
            for start in range(10 - length):
                num = int(digits[start : start + length])
                
                # Check if the generated number falls within the range
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    # Minor optimization: if the number exceeds high, 
                    # larger numbers of this length will also exceed it.
                    break 
                    
        return sorted(result)