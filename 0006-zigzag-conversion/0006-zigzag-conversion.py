class Solution:

    def convert(self, s: str, numRows: int) -> str:
        # Base case: no zigzag possible if only 1 row or string is short
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a bucket for each row
        rows = ["" for _ in range(numRows)]

        current_row = 0
        going_down = False  # Track vertical direction

        # Distribute characters into rows
        for char in s:
            rows[current_row] += char

            # Reverse direction at top (0) or bottom (numRows - 1)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            current_row += 1 if going_down else -1

        # Merge rows to read line by line
        return "".join(rows)
