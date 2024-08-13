class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(str(i) for i in digits))
        res = res + 1
        return [int(i) for i in str(res)]

'''
convert list into integer 
then add 1
then convert integer into list
'''
