class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Option 1: Buy 0 type 3 items (use only type 1 and type 2)
        ans1 = need1 * cost1 + need2 * cost2
        
        # Option 2: Buy min(need1, need2) type 3 items, then cover the remainder individually
        common = min(need1, need2)
        ans2 = common * costBoth + (need1 - common) * cost1 + (need2 - common) * cost2
        
        # Option 3: Buy max(need1, need2) type 3 items to cover everything
        ans3 = max(need1, need2) * costBoth
        
        return min(ans1, ans2, ans3)
