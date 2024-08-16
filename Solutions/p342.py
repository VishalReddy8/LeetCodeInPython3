class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n>1): 
            while(n%4==0):
                n//=4
        if n == 1:
            return True
        else:
            return False
'''
Same as 326,self explanatory
'''
