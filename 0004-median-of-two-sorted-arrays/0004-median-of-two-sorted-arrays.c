double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }
    
    int m = nums1Size;
    int n = nums2Size;
    int low = 0;
    int high = m;
    
    while (low <= high) {
        int partitionX = low + (high - low) / 2;
        int partitionY = (m + n + 1) / 2 - partitionX;
        
        // Handle edge conditions when partition falls on the boundaries
        int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];
        
        int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];
        
        // Correct partition found
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            // If total number of elements is odd
            if ((m + n) % 2 != 0) {
                return (double)MAX(maxLeftX, maxLeftY);
            }
            // If total number of elements is even
            return ((double)MAX(maxLeftX, maxLeftY) + MIN(minRightX, minRightY)) / 2.0;
        }
        else if (maxLeftX > minRightY) {
            // Move left in nums1
            high = partitionX - 1;
        }
        else {
            // Move right in nums1
            low = partitionX + 1;
        }
    }
    
    return 0.0;
}