# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        list1 = []
        while(current1):
            list1.append(str(current1.val))
            current1 = current1.next
        current2 = l2
        list2 = []
        while(current2):
            list2.append(str(current2.val))
            current2 = current2.next
        
        list1.reverse()
        list2.reverse()
        
        res1 = int("".join(list1))
        res2 = int("".join(list2))
        res = res1 + res2
        result = [int(x) for x in str(res)]
        
        # Create a linked list from the result
        dummy = ListNode(0)
        current = dummy
        for val in reversed(result):
            current.next = ListNode(val)
            current = current.next
        return dummy.next


'''
traverse the linkedlist, store values in list, reverse the list,convert into integer, add the values, convert into list, reverse the list, return linkedlist
'''
