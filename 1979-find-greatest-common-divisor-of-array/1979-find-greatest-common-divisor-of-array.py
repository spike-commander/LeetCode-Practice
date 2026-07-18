class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the smallest and largest numbers
        min_num = min(nums)
        max_num = max(nums)
        
        # Return their greatest common divisor
        return math.gcd(min_num, max_num)