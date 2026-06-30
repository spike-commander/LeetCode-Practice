class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
    
        for i, num in enumerate(nums):
            complement = target - num
        
        # Check if the complement is already found
            if complement in seen:
                return [seen[complement], i]
        
        # Store the index of the current number
            seen[num] = i
        
        return []