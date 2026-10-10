class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_rights = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Each '(' requires 2 consecutive ')'
                needed_rights += 2
                
                # If we had an odd number of needed_rights from a previous single ')',
                # it means that single ')' can never find a consecutive pair. 
                # We must insert 1 right parenthesis to balance it immediately.
                if needed_rights % 2 != 0:
                    insertions += 1
                    needed_rights -= 1
                i += 1
            else:
                # We encountered a ')'
                # Check if it forms a pair with the next character
                if i + 1 < n and s[i + 1] == ')':
                    # Consecutive '))' found
                    if needed_rights >= 2:
                        needed_rights -= 2
                    else:
                        # No matching '(' exists, so we must insert 1 '('
                        insertions += 1
                    i += 2  # Skip both ')'
                else:
                    # Single ')' found
                    if needed_rights >= 2:
                        needed_rights -= 1
                    else:
                        # No matching '(' exists. We need 1 '(' and 1 more ')'
                        insertions += 2
                    i += 1
                    
        # Any remaining needed right parentheses must be added at the end
        return insertions + needed_rights
