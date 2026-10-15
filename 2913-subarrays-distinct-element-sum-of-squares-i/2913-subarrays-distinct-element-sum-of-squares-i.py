class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment Tree arrays for lazy propagation
        # tree_sum stores the sum of x
        # tree_sq_sum stores the sum of x^2
        # lazy stores the increment value to be propagated
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_down(node, start, end):
            if lazy[node] == 0:
                return
            
            mid = (start + end) // 2
            left_len = mid - start + 1
            right_len = end - mid
            
            val = lazy[node]
            
            # Update left child
            tree_sq_sum[2 * node] = (tree_sq_sum[2 * node] + 2 * val * tree_sum[2 * node] + val * val * left_len) % MOD
            tree_sum[2 * node] = (tree_sum[2 * node] + val * left_len) % MOD
            lazy[2 * node] = (lazy[2 * node] + val) % MOD
            
            # Update right child
            tree_sq_sum[2 * node + 1] = (tree_sq_sum[2 * node + 1] + 2 * val * tree_sum[2 * node + 1] + val * val * right_len) % MOD
            tree_sum[2 * node + 1] = (tree_sum[2 * node + 1] + val * right_len) % MOD
            lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % MOD
            
            lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l <= start and end <= r:
                # Update rule for squared sum: (x + val)^2 = x^2 + 2*val*x + val^2
                segment_len = end - start + 1
                tree_sq_sum[node] = (tree_sq_sum[node] + 2 * val * tree_sum[node] + val * val * segment_len) % MOD
                tree_sum[node] = (tree_sum[node] + val * segment_len) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push_down(node, start, end)
            mid = (start + end) // 2
            
            if l <= mid:
                update(2 * node, start, mid, l, r, val)
            if r > mid:
                update(2 * node + 1, mid + 1, end, l, r, val)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[2 * node] + tree_sq_sum[2 * node + 1]) % MOD

        total_ans = 0
        last_seen = {}
        
        # Traverse through the array tracking the contribution of each element
        for i, num in enumerate(nums):
            # If the element was seen before, it only adds a new distinct count 
            # to subarrays starting after its last occurrence.
            prev_idx = last_seen.get(num, -1)
            
            # Increment the distinct count by 1 for all valid subarrays ending at index i
            update(1, 0, n - 1, prev_idx + 1, i, 1)
            
            # tree_sq_sum[1] holds the total sum of squared distinct counts for all subarrays ending at i
            total_ans = (total_ans + tree_sq_sum[1]) % MOD
            last_seen[num] = i
            
        return total_ans
