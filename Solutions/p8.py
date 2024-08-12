class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) > 200:
            return 0
        s = s.lstrip(" ")
        if not s:
            return 0
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        res = []
        for i in s:
            if i.isnumeric():
                res.append(i)
            else:
                break
        if not res:
            return 0
        result = int("".join(res))
        if negative:
            result = -result
        if result < -pow(2,31):
            return -pow(2,31)
        if result > pow(2,31) - 1:
            return pow(2,31) - 1
        return result 

'''
convert into list and solve approach, lstrip = left strip -> removes left hand side blank spaces
'''
