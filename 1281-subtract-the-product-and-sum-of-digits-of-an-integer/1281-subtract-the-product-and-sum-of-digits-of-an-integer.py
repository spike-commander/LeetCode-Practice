class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        Sum = 0
        List = [int(i) for i in str(n)]
        for i in range(len(List)):
            prod*=List[i]
            Sum+=List[i]
        return prod - Sum