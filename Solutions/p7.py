class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            negative = True
            x = abs(x)
        else:
            negative = False
        res = [i for i in str(x)]
        res.reverse()
        result = int("".join(res))
        if(result < pow(2,31) - 1 and result >pow(2,31)*-1):
            if(negative):
                return result*(-1)
            else:
                return result
        else:
            return 0
  '''
  Simple Maths, can make the code smaller converting number into string instead of list and then string and then number
  '''
