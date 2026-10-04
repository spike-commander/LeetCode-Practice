class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open tracks the minimum possible open '(' we must carry
        # max_open tracks the maximum possible open '(' we could carry
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                min_open -= 1  # If treated as ')'
                max_open += 1  # If treated as '('
            
            # If max_open is negative, we have more ')' than possible '(' + '*'
            if max_open < 0:
                return False
            
            # min_open cannot drop below 0 because we can choose to treat 
            # excess '*' as empty strings or '(' instead of closing brackets.
            if min_open < 0:
                min_open = 0
                
        # If 0 is within our valid range [min_open, max_open], the string is valid
        return min_open == 0
