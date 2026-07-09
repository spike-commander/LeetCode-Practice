class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component_id = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # Step 2: Answer each query in O(1) time
        ans = []
        for u, v in queries:
            ans.append(component_id[u] == component_id[v])
            
        return ans