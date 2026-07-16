import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        current_max = 0
        
        # Step 1: Construct prefixGcd array
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(num, current_max))
        
        # Step 2: Sort the array in non-decreasing order
        prefixGcd.sort()
        
        # Step 3: Pair smallest and largest elements using two pointers
        total_gcd_sum = 0
        left, right = 0, len(prefixGcd) - 1
        
        while left < right:
            total_gcd_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum
