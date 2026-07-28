from typing import List
from collections import defaultdict

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # 1. Filter edges: Keep only edges where both source and destination are online
        # Collect all unique edge costs to use as candidates for our binary search
        valid_edges = []
        unique_costs = set()
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
                unique_costs.add(cost)
        
        # Sort the unique costs to perform an efficient binary search
        sorted_costs = sorted(list(unique_costs))
        
        # 2. Build adjacency list and find topological order
        # Since it's a DAG, we can find a valid topological sort considering only valid nodes
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        nodes_in_graph = set()
        
        for u, v, cost in valid_edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            nodes_in_graph.add(u)
            nodes_in_graph.add(v)
            
        # Standard Kahn's algorithm for Topological Sort
        # We only need to process nodes that are reachable or part of the valid graph
        queue = [i for i in range(n) if online[i] and in_degree[i] == 0]
        topo_order = []
        
        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            for neighbor, _ in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 3. Helper function to check if a path with min_edge_cost >= X is possible within cost k
        def can_achieve_score(min_cost_threshold: int) -> bool:
            # dp[i] stores the minimum total cost to reach node i from node 0
            dp = {}
            dp[0] = 0
            
            for node in topo_order:
                if node not in dp:
                    continue
                
                current_total_cost = dp[node]
                for neighbor, edge_cost in adj[node]:
                    # Only consider edges that meet or exceed our target minimum edge cost threshold
                    if edge_cost >= min_cost_threshold:
                        new_total_cost = current_total_cost + edge_cost
                        if neighbor not in dp or new_total_cost < dp[neighbor]:
                            dp[neighbor] = new_total_cost
            
            # Check if destination is reached and total path cost is within budget k
            return n - 1 in dp and dp[n - 1] <= k

        # 4. Binary search over the available unique edge costs
        left, right = 0, len(sorted_costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            X = sorted_costs[mid]
            
            if can_achieve_score(X):
                ans = X          # This score is possible, try to find a larger one
                left = mid + 1
            else:
                right = mid - 1  # Cannot achieve this score, look for a smaller one
                
        return ans
