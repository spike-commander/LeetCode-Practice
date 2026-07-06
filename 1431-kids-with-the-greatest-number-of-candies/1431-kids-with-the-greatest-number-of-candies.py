class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        List = []
        Max = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= Max:
                List.append(True)
            else:
                List.append(False)
        return List