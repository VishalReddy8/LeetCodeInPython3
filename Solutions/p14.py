class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans = ans + first[i]
        return ans


'''
Sort and compare first n last
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the list of strings
        strs.sort()

        # Compare the first and last string only
        first_str = strs[0]
        last_str = strs[-1]
        common_prefix = ""

        # Loop through characters until mismatch or shortest length
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] != last_str[i]:
                break
            common_prefix += first_str[i]

        return common_prefix

