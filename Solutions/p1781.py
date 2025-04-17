class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0 
        n = len(s)
        for i in range(n): 
            d = dict()
            for j in range(i,n):
                if s[j] in d:
                    d[s[j]] += 1 
                else:
                    d[s[j]] = 1 

                a = max(d.values())
                b = min(d.values())

                beauty += (a-b)

        return beauty         
