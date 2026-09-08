class Solution:
    def countCommas(self, n: int) -> int:
        # Numbers below 1000 have 0 commas.
        # Numbers from 1000 to n each have exactly 1 comma.
        if n < 1000:
            return 0
        return n - 999
