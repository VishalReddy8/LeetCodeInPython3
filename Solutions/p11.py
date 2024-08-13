class Solution:
    def maxArea(self, height: List[int]) -> i
        i = 0
        j = len(height) - 1
        max_area = 0
        while(i<j):
            width = j-i
            if height[i] < height[j]:
                curr = height[i]
                i  = i + 1
            else:
                curr = height[j]
                j = j - 1
            curr_area = curr*width
            max_area = max(max_area,curr_area)
        return max_area

'''
two pointer approach, similar code to quick sort
'''
