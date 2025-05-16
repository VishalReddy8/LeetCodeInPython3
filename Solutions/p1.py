class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums): 
            if target - num in nums_dict:  
                return [nums_dict[target - num], i]  
            nums_dict[num] = i

''' 
enumeration of list num will give values 0,1,2,3.. to i and values of list to num 

while adding to dictionary keys are the num values and values are the i values

target = (target - num) + num

return the index values of (target - num) and num

there are many more approaches that we can use 

like two pointer and dict without enum 
'''
