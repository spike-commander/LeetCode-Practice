class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year (1-365)
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum days of all previous months plus current days
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all arrival and departure dates to integers
        start_A = date_to_day(arriveAlice)
        end_A = date_to_day(leaveAlice)
        start_B = date_to_day(arriveBob)
        end_B = date_to_day(leaveBob)
        
        # Find the overlapping interval
        overlap_start = max(start_A, start_B)
        overlap_end = min(end_A, end_B)
        
        # Calculate overlapping days (inclusive)
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0
