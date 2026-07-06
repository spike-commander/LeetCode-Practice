from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point ascending, and by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current interval extends past the maximum end seen so far,
            # it cannot be completely covered by any previous interval.
            if end > max_end:
                remaining += 1
                max_end = end
                
        return remaining
