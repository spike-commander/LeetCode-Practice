class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate the absolute difference for each pair
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total_k = k1 + k2
        
        # If the total k is greater than or equal to the sum of all differences,
        # we can reduce all differences down to 0.
        if sum(diffs) <= total_k:
            return 0
            
        # Use a bucket array to count frequencies of each difference value.
        # Max possible difference is bounded by 10^5 based on constraints.
        max_diff = max(diffs)
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
            
        # Greedily shift frequencies from the highest differences downwards
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
            
            # Number of operations needed to decrement all elements of size d to d-1
            needed = buckets[d]
            if total_k >= needed:
                total_k -= needed
                buckets[d - 1] += buckets[d]
                buckets[d] = 0
            else:
                # We can only partially reduce some elements of size d
                buckets[d - 1] += total_k
                buckets[d] -= total_k
                total_k = 0
                break
                
        # Calculate the final sum of squared differences
        return sum(count * (d ** 2) for d, count in enumerate(buckets))
