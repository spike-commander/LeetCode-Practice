class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Extract prime factor counts (2, 3, 5, 7) from t
        rem_t = t
        target_cnt = [0, 0, 0, 0]  # indices map to [2, 3, 5, 7]
        primes = [2, 3, 5, 7]
        
        for i, p in enumerate(primes):
            while rem_t % p == 0:
                target_cnt[i] += 1
                rem_t //= p
                
        # If t has any other prime factors (like 11, 13), it's impossible
        if rem_t > 1:
            return "-1"

        def get_min_digits_needed(cnt):
            """Computes the absolute minimum digits needed to satisfy factor counts exactly."""
            c2, c3, c5, c7 = [max(0, x) for x in cnt]
            mandatory_digits = c5 + c7
            best_23_digits = float('inf')
            
            # Check all possible variations of combining 2 and 3 using digit '6'
            limit_6 = min(c2, c3)
            for n6 in range(limit_6 + 1):
                rem_c2 = c2 - n6
                rem_c3 = c3 - n6
                
                n9 = rem_c3 // 2
                left_c3 = rem_c3 % 2
                
                n8 = rem_c2 // 3
                left_c2 = rem_c2 % 3
                
                extra = 0
                if left_c3 == 1:
                    if left_c2 == 1: 
                        extra = 1     # Combined into a single '6'
                    elif left_c2 == 2: 
                        extra = 2     # Formed into '6' and '2' (or '3' and '4')
                    elif left_c2 == 0: 
                        extra = 1     # Leftover single '3'
                else:
                    if left_c2 == 1: 
                        extra = 1     # Leftover single '2'
                    elif left_c2 == 2: 
                        extra = 1     # Combined into a single '4'
                    elif left_c2 == 0: 
                        extra = 0
                
                total_23 = n6 + n9 + n8 + extra
                if total_23 < best_23_digits:
                    best_23_digits = total_23
                    
            return mandatory_digits + best_23_digits

        def fill_optimal_suffix(length, cnt):
            """Fills the suffix position-by-position to guarantee the lexicographically smallest value."""
            cur_cnt = list(cnt)
            res = []
            for pos in range(length):
                rem_len = length - 1 - pos
                # Greedily try smallest digits first (1 to 9)
                for nxt_d in range(1, 10):
                    next_cnt = list(cur_cnt)
                    d_temp = nxt_d
                    for p_idx, p in enumerate(primes):
                        while d_temp % p == 0 and d_temp > 0:
                            next_cnt[p_idx] -= 1
                            d_temp //= p
                    
                    if get_min_digits_needed(next_cnt) <= rem_len:
                        res.append(str(nxt_d))
                        cur_cnt = next_cnt
                        break
            return "".join(res)

        n = len(num)
        
        # Step 2: Track remaining factors prefix-by-prefix
        rem_cnt = [list(target_cnt)]
        first_zero = -1
        
        for i in range(n):
            if num[i] == '0':
                first_zero = i
                break
            
            curr = list(rem_cnt[-1])
            digit = int(num[i])
            for p_idx, p in enumerate(primes):
                d_temp = digit
                while d_temp % p == 0 and d_temp > 0:
                    curr[p_idx] -= 1
                    d_temp //= p
            rem_cnt.append(curr)

        # Case 1: Original 'num' itself is already zero-free and valid
        if first_zero == -1 and all(x <= 0 for x in rem_cnt[-1]):
            return num

        start_pos = first_zero if first_zero != -1 else n - 1

        # Case 2: Backtrack from right to left to find a position to change
        for i in range(start_pos, -1, -1):
            start_digit = int(num[i]) + 1
            for d in range(start_digit, 10):
                current_rem = list(rem_cnt[i])
                d_temp = d
                for p_idx, p in enumerate(primes):
                    while d_temp % p == 0:
                        current_rem[p_idx] -= 1
                        d_temp //= p
                
                rem_len = n - 1 - i
                if get_min_digits_needed(current_rem) <= rem_len:
                    prefix = num[:i] + str(d)
                    suffix = fill_optimal_suffix(rem_len, current_rem)
                    return prefix + suffix

        # Case 3: Same length is structurally impossible, generate a longer sequence
        total_len = get_min_digits_needed(target_cnt)
        new_len = max(total_len, n + 1)
        return fill_optimal_suffix(new_len, target_cnt)
