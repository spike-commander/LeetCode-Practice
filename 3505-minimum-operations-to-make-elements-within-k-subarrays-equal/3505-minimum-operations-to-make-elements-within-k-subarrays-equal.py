import heapq
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Max-heap for the smaller half (invert signs for max-heap behavior)
        left_h = []   
        # Min-heap for the larger half
        right_h = []  
        
        left_sum = 0
        right_sum = 0
        left_size = 0
        right_size = 0
        
        # Lazy deletion maps for sliding window elements
        del_left = Counter()
        del_right = Counter()
        
        # Precomputed operations cost for each window of size x
        cost = [0] * (n - x + 1)
        
        def balance():
            nonlocal left_sum, right_sum, left_size, right_size
            
            # Prune out-of-window elements from the top of left_h
            while left_h and del_left[-left_h[0]] > 0:
                del_left[-left_h[0]] -= 1
                heapq.heappop(left_h)
            # Prune out-of-window elements from the top of right_h
            while right_h and del_right[right_h[0]] > 0:
                del_right[right_h[0]] -= 1
                heapq.heappop(right_h)
                
            # Target size of the lower half (median split point)
            target_left = (x + 1) // 2
            
            # Balance elements from left to right if left is too large
            while left_size > target_left:
                val = -heapq.heappop(left_h)
                if del_left[val] > 0:
                    del_left[val] -= 1
                else:
                    heapq.heappush(right_h, val)
                    left_sum -= val
                    right_sum += val
                    left_size -= 1
                    right_size += 1
                    
            # Balance elements from right to left if left is too small
            while left_size < target_left and right_size > 0:
                val = heapq.heappop(right_h)
                if del_right[val] > 0:
                    del_right[val] -= 1
                else:
                    heapq.heappush(left_h, -val)
                    right_sum -= val
                    left_sum += val
                    left_size += 1
                    right_size -= 1
                    
            # Final pruning after structural transfers
            while left_h and del_left[-left_h[0]] > 0:
                del_left[-left_h[0]] -= 1
                heapq.heappop(left_h)
            while right_h and del_right[right_h[0]] > 0:
                del_right[right_h[0]] -= 1
                heapq.heappop(right_h)

        def add(val):
            nonlocal left_sum, right_sum, left_size, right_size
            if not left_h or val <= -left_h[0]:
                heapq.heappush(left_h, -val)
                left_sum += val
                left_size += 1
            else:
                heapq.heappush(right_h, val)
                right_sum += val
                right_size += 1
            balance()

        def remove(val):
            nonlocal left_sum, right_sum, left_size, right_size
            if val <= -left_h[0]:
                del_left[val] += 1
                left_sum -= val
                left_size -= 1
            else:
                del_right[val] += 1
                right_sum -= val
                right_size -= 1
            balance()

        # Phase 1: Compute window absolute deviation costs in O(N log X)
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                median = -left_h[0]
                # Mathematical absolute difference breakdown:
                # Sum(|val - median|) = (right_sum - right_count*median) + (left_count*median - left_sum)
                op_cost = right_sum - left_sum + median * (left_size - right_size)
                cost[i - x + 1] = op_cost

        # Phase 2: Complete the sequence selection via DP in O(N * K)
        # Using a flattened row or direct lookup to optimize pointer references
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Choice 1: Skip the current element
                dp[i][j] = dp[i - 1][j]
                
                # Choice 2: Complete a size-x window matching group j at index i-1
                if i >= x:
                    prev_cost = dp[i - x][j - 1]
                    if prev_cost != float('inf'):
                        current_window_cost = cost[i - x] + prev_cost
                        if current_window_cost < dp[i][j]:
                            dp[i][j] = current_window_cost
                            
        return dp[n][k]
