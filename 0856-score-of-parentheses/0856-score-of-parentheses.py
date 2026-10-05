class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # If the current ')' immediately follows a '(', it is a core "()"
                if s[i - 1] == '(':
                    score += 1 << depth  # 1 << depth is equivalent to 2^depth
                    
        return score
