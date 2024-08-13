class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]

'''
sum[2:0] because starting of binary string contains 0b or 1b for sign n type
'''
