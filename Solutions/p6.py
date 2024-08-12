class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [''] * numRows
        index, step = 0, 1

        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(res)

'''
Matrix or Matrix i,e. array(char)(char) or array(string)
the pattern for n rows can be give as
1 2 3 4 ... n ... 4 3 2 1 2 3 4 ... n ... 4 3 2 1
in the problem we are using
0 1 2 .. n-1 .. 2 1 0 1 2 ... n-1 ... 2 1 0
'''
