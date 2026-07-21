from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Augment the string as specified
        t = '1' + s + '1'
        
        # Represent t as a list of [char, block_length]
        blocks = [[char, len(list(group))] for char, group in groupby(t)]
        
        total_ones = s.count('1')
        max_ones = total_ones
        
        # Collect all '0' blocks with their indices to track position
        zero_blocks = []
        for i, (char, length) in enumerate(blocks):
            if char == '0':
                zero_blocks.append((length, i))
                
        # Keep up to the top 3 largest '0' blocks to avoid overlapping
        zero_blocks.sort(key=lambda x: x[0], reverse=True)
        top_zeros = zero_blocks[:3]
        
        # Iterate through internal '1' blocks (must be surrounded by '0's)
        # Thus, index cannot be 0 or len(blocks) - 1
        for i in range(1, len(blocks) - 1):
            if blocks[i][0] == '1':
                X_len = blocks[i][1]
                L_len = blocks[i - 1][1]
                R_len = blocks[i + 1][1]
                
                # Choice 1: Flip the newly merged block (L + X + R) back to '1's
                max_ones = max(max_ones, total_ones + L_len + R_len)
                
                # Choice 2: Flip a different independent '0' block
                for z_len, z_idx in top_zeros:
                    if z_idx != i - 1 and z_idx != i + 1:
                        max_ones = max(max_ones, total_ones - X_len + z_len)
                        break  # Since top_zeros is sorted, the first match yields the max
                        
        return max_ones
