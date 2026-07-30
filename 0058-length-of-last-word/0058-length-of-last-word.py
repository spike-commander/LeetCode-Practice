class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()
        return len(result[-1])