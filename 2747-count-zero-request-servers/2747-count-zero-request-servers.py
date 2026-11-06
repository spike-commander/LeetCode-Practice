from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda log: log[1])
        
        # Store queries with their original indices and sort them by time
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        unique_servers = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for original_idx, q in sorted_queries:
            # Add logs that enter the window [q - x, q] from the right
            while right < m and logs[right][1] <= q:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    unique_servers += 1
                server_counts[server_id] += 1
                right += 1
                
            # Remove logs that fall out of the window [q - x, q] from the left
            while left < m and logs[left][1] < q - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    unique_servers -= 1
                left += 1
                
            # Servers that received no requests = Total servers - Servers with active requests
            ans[original_idx] = n - unique_servers
            
        return ans
