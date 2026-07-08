class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Filter out all non-zero digits and keep track of their original indices
        nz_chars = []
        nz_orig_indices = []
        for i, ch in enumerate(s):
            if ch != '0':
                nz_chars.append(ch)
                nz_orig_indices.append(i)
                
        k = len(nz_chars)
        
        # 2. Precompute powers of 10 modulo MOD for the filtered length
        p10 = [1] * (k + 1)
        for i in range(1, k + 1):
            p10[i] = (p10[i - 1] * 10) % MOD
            
        # 3. Precompute prefix numbers for the filtered string
        pref_val = [0] * (k + 1)
        for i in range(k):
            pref_val[i + 1] = (pref_val[i] * 10 + int(nz_chars[i])) % MOD
            
        # 4. Precompute simple prefix sums of the original string digits
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + int(s[i])
            
        ans = []
        for l, r in queries:
            # Find boundary bounds of non-zero indices falling within [l, r]
            L_nz = bisect.bisect_left(nz_orig_indices, l)
            R_nz = bisect.bisect_right(nz_orig_indices, r) - 1
            
            # If valid non-zero elements exist inside the query range
            if L_nz <= R_nz:
                x = (pref_val[R_nz + 1] - pref_val[L_nz] * p10[R_nz - L_nz + 1]) % MOD
            else:
                x = 0
                
            # Digit sum is unchanged whether zeros are included or omitted
            digit_sum = pref_sum[r + 1] - pref_sum[l]
            
            ans.append((x * digit_sum) % MOD)
            
        return ans