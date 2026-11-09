from heapq import heappush, heappop
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Track how many requests each server successfully handles
        request_count = [0] * k
        
        # Pool of available servers (starts with all servers 0 to k-1)
        available = SortedList(range(k))
        
        # Min-heap to track busy servers: stores tuples of (free_time, server_id)
        busy = []
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            # 1. Free up all servers that have finished their tasks by the current arrival time
            while busy and busy[0][0] <= start:
                _, server_id = heappop(busy)
                available.add(server_id)
            
            # 2. If no servers are available, the request is dropped
            if not available:
                continue
            
            # 3. Find the target server index (i % k)
            target = i % k
            
            # Find the first available server ID >= target
            idx = available.bisect_left(target)
            
            # If no server ID >= target exists, wrap around to the beginning of the available pool
            if idx == len(available):
                idx = 0
                
            chosen_server = available.pop(idx)
            
            # 4. Record the assignment
            request_count[chosen_server] += 1
            heappush(busy, (start + duration, chosen_server))
            
        # Find the maximum requests handled by any server
        max_requests = max(request_count)
        
        # Return all server IDs that achieved this maximum
        return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
