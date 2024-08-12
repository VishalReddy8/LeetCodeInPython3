class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x > pow(2,31) - 1 and x < pow(2,31)*-1):
            return False
        string = str(x)
        i = 0
        j = len(string) - 1
        while(i<j):
            if(string[i] !=string[j]):
                return False
            i = i + 1
            j = j - 1
        return True

'''
Two pointer approach
'''
