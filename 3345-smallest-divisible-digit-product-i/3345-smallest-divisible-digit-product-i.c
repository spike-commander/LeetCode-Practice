int smallestNumber(int n, int t) {
    while (1) {
        int temp = n;
        long long product = 1;
        
        // Handle 0 separately, though n >= 1 based on constraints
        if (temp == 0) {
            product = 0;
        } else {
            while (temp > 0) {
                product *= (temp % 10);
                temp /= 10;
            }
        }
        
        // Check if the product of digits is divisible by t
        if (product % t == 0) {
            return n;
        }
        
        n++; // Move to the next number
    }
}
