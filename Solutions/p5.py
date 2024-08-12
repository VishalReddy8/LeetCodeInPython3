class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if len(s) == 0:
            return ""
        
        longest = s[0]
        for i in range(len(s)):
            palindrome1 = expand_around_center(s, i, i)
            palindrome2 = expand_around_center(s, i, i + 1)  
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        return longest
'''
def expand_around_center will return palindrom value, we return s[left+1:right] right-1 is not needed because string slicing doesnt add s[right] anyways
longest variable stores the value of palindrome
'''
