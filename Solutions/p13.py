class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        num = 0
        symbol = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        for i in range(len(s)):
            num = symbol[s[i]]
            if i + 1 < len(s) and symbol[s[i + 1]] > num:
                ans = ans - num
            else:
                ans = ans + num
        return ans
'''
Maths
if the next symbol in string has greater value then subtract else add
'''
