from bisect import bisect_right
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Collect and sort all unique values present in the graph
        sorted_vals = sorted(list(set(nums)))
        m = len(sorted_vals)
        
        # Map each value to its index position in the sorted array
        val_to_idx = {val: i for i, val in enumerate(sorted_vals)}
        
        # Step 2: For each unique value, find the index of the furthest element it can reach on its right
        # using a binary search/sliding window approach
        next_jump = [0] * m
        for i in range(m):
            # Find the largest index j such that sorted_vals[j] - sorted_vals[i] <= maxDiff
            limit = sorted_vals[i] + maxDiff
            idx = bisect_right(sorted_vals, limit) - 1
            next_jump[i] = idx
            
        # Step 3: Construct the Binary Lifting (Successor Graph) table
        # 18 levels are sufficient since 2^17 = 131,072 > 10^5 constraints
        LOG = 18
        up = [[0] * m for _ in range(LOG)]
        
        for i in range(m):
            up[0][i] = next_jump[i]
            
        for j in range(1, LOG):
            for i in range(m):
                up[j][i] = up[j - 1][up[j - 1][i]]
                
        # Step 4: Process queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1)
                continue
                
            # Keep track of sorted index endpoints (left to right transition)
            idx_u = val_to_idx[val_u]
            idx_v = val_to_idx[val_v]
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
                
            # If the ultimate jump from idx_u cannot even reach idx_v, they are completely disconnected
            if up[LOG - 1][idx_u] < idx_v:
                ans.append(-1)
                continue
                
            # Accumulate steps using binary lifting
            steps = 0
            curr = idx_u
            for j in range(LOG - 1, -1, -1):
                if up[j][curr] < idx_v:
                    curr = up[j][curr]
                    steps += (1 << j)
            
            # One final step bridges the last gap or lands perfectly on target
            ans.append(steps + 1)
            
        return ans
