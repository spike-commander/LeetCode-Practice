class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str: str, open_count: int, close_count: int):
            # Base case: valid combination found
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Add an open parenthesis if we haven't reached the limit 'n'
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Add a close parenthesis if it safely matches an open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result
