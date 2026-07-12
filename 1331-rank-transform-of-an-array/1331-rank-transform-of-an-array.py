class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Remove duplicates and sort to find the relative order
        sorted_unique = sorted(set(arr))
        
        # Step 2: Map each unique element to its 1-based rank
        rank_map = {num: rank for rank, num in enumerate(sorted_unique, start=1)}
        
        # Step 3: Replace each original element with its rank
        return [rank_map[num] for num in arr]