class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(c) - 64) * (26 ** i) for i, c in enumerate(reversed(columnTitle)))

'''
Reverse because list starts from left to right and not right to left

enumerate to get index and char together

ord() for ASCII conversion
'''
