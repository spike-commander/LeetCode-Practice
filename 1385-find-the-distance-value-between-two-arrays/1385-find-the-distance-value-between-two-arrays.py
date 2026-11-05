import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort arr2 to enable binary search
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Look for the first element in arr2 that is >= x - d
            idx = bisect.bisect_left(arr2, x - d)
            
            # If such an element exists and is also <= x + d, 
            # it falls within the invalid range [x - d, x + d]
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
            
            # If no element in arr2 is within the range, increment count
            distance_value += 1
            
        return distance_value
