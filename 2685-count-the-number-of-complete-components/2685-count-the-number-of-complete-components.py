from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components_count = 0
        
        # Traverse every vertex to find all connected components
        for i in range(n):
            if not visited[i]:
                # Start a BFS to explore the current component
                queue = deque([i])
                visited[i] = True
                
                component_vertices = []
                
                while queue:
                    curr = queue.popleft()
                    component_vertices.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Check if the component is complete
                # Each vertex in a complete component must have a degree of (V - 1)
                num_vertices = len(component_vertices)
                is_complete = True
                
                for vertex in component_vertices:
                    if len(adj[vertex]) != num_vertices - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count
