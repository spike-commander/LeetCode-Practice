import sys

# Increase recursion depth for deep tree structures
sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Setup variables for Euler Tour and Binary Lifting (LCA)
        LOGN = 17  # Since 2^16 = 65536 > 5*10^4
        up = [[0] * LOGN for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        timer = 0
        
        initial_node_masks = [0] * n
        s_list = list(s)
        
        # DFS to compute entry/exit times, depth, and prefix XOR masks from root
        def dfs(u, p, current_mask):
            nonlocal timer
            tin[u] = timer
            timer += 1
            
            char_bit = 1 << (ord(s_list[u]) - ord('a'))
            current_mask ^= char_bit
            initial_node_masks[u] = current_mask
            
            up[u][0] = p
            for i in range(1, LOGN):
                up[u][i] = up[up[u][i-1]][i-1]
                
            for v in adj[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u, current_mask)
            tout[u] = timer - 1

        dfs(0, 0, 0)
        
        # 3. Binary Indexed Tree (Fenwick Tree) for Range XOR updates
        bit_tree = [0] * (timer + 1)
        
        def bit_update(idx, val):
            idx += 1
            while idx <= timer:
                bit_tree[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit_tree[idx]
                idx -= idx & (-idx)
            return res
            
        def range_update(l, r, val):
            bit_update(l, val)
            bit_update(r + 1, val)
            
        # 4. Binary Lifting function to find LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOGN):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOGN - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # Helper to isolate the single active character bit at a node
        def get_current_node_mask(u):
            mask_u = initial_node_masks[u] ^ bit_query(tin[u])
            if u == 0:
                return mask_u
            p = up[u][0]
            mask_p = initial_node_masks[p] ^ bit_query(tin[p])
            return mask_u ^ mask_p

        # 5. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                
                old_char_mask = get_current_node_mask(u)
                new_char_mask = 1 << (ord(new_char) - ord('a'))
                
                xor_diff = old_char_mask ^ new_char_mask
                if xor_diff != 0:
                    # Update the entire subtree of node u
                    range_update(tin[u], tout[u], xor_diff)
                    
            else:  # "query"
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                
                # Fetch root-to-node path masks with active modifications applied
                mask_u = initial_node_masks[u] ^ bit_query(tin[u])
                mask_v = initial_node_masks[v] ^ bit_query(tin[v])
                mask_lca_char = get_current_node_mask(lca)
                
                # Combine paths using XOR
                path_mask = mask_u ^ mask_v ^ mask_lca_char
                
                # Palindrome check: verify if at most 1 bit is set
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans
