class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        res.append(1)
        ans = 1
        for i in range(1,rowIndex+1):
            ans *= (rowIndex +1 - i)
            ans //= i
            res.append(ans)
        return res
'''
rowIndex + 1 because we started count from 0th index
'''
