class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track the two largest numbers
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                max2 = max1  # Current max becomes the second max
                max1 = num   # Update the largest max
            elif num > max2:
                max2 = num   # Update the second largest max
                
        return (max1 - 1) * (max2 - 1)
