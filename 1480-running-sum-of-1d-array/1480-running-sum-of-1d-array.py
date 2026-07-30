class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = nums[0]
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(Sum+nums[i])
            Sum+=nums[i]
        return ans