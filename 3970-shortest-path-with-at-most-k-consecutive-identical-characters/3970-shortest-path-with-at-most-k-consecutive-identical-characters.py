import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][c] stores the minimum cost to reach node u 
        # with c consecutive identical characters ending at u.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Priority queue stores tuples of (cost, current_node, consecutive_count)
        # Start at node 0, cost 0, consecutive count 1 (accounting for labels[0])
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            cost, u, consecutive_count = heapq.heappop(pq)
            
            # Since Dijkstra's pops the minimum cost first, reaching n - 1 here is optimal
            if u == n - 1:
                return cost
                
            # If we found a shorter path to this state already, skip it
            if cost > dist[u][consecutive_count]:
                continue
                
            # Explore neighbors
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    new_count = consecutive_count + 1
                else:
                    new_count = 1
                    
                # Check if the new state satisfies the consecutive constraint 
                # and offers a strictly cheaper path
                if new_count <= k and cost + w < dist[v][new_count]:
                    dist[v][new_count] = cost + w
                    heapq.heappush(pq, (cost + w, v, new_count))
                    
        return -1
