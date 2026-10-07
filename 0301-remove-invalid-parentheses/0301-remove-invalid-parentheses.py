class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Calculate the exact number of misplaced '(' and ')'
        rem_left = 0
        rem_right = 0
        
        for char in s:
            if char == '(':
                rem_left += 1
            elif char == ')':
                if rem_left > 0:
                    rem_left -= 1
                else:
                    rem_right += 1
                    
        result = set()
        
        # Helper to validate if a string has balanced parentheses
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(': count += 1
                elif char == ')': count -= 1
                if count < 0: return False
            return count == 0

        # Step 2: Backtracking function
        def backtrack(index: int, left_count: int, right_count: int, 
                      left_rem: int, right_rem: int, current_path: list[str]):
            # Base Case: Reached the end of the string
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    joined_str = "".join(current_path)
                    if isValid(joined_str):
                        result.add(joined_str)
                return

            char = s[index]

            # Optimization to avoid duplicate branches on identical consecutive characters
            # e.g., if we have "(((", removing the 1st, 2nd, or 3rd yields the same branch
            is_duplicate = (index > 0 and char == s[index - 1])

            # Option 1: Try discarding the current character (if valid to do so)
            if char == '(' and left_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem - 1, right_rem, current_path)
            elif char == ')' and right_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem, right_rem - 1, current_path)

            # Option 2: Try keeping the current character
            current_path.append(char)
            if char not in ('(', ')'):
                # Non-parenthesis characters are always kept
                backtrack(index + 1, left_count, right_count, left_rem, right_rem, current_path)
            else:
                # Keep parenthesis if it doesn't instantly violate prefix validity
                if char == '(':
                    backtrack(index + 1, left_count + 1, right_count, left_rem, right_rem, current_path)
                elif right_count < left_count:
                    backtrack(index + 1, left_count, right_count + 1, left_rem, right_rem, current_path)
            
            # Backtrack (Undo state change)
            current_path.pop()

        # Step 3: Trigger the backtracking process
        backtrack(0, 0, 0, rem_left, rem_right, [])
        return list(result)
