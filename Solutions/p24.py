# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy 
        cur = head
        while cur and cur.next:
            temp = cur.next.next
            first = cur 
            second = cur.next
            
            second.next = first
            first.next = temp 
            
            prev.next = second
            prev = cur
            cur = temp 

        return dummy.next


'''
Better to draw it to visulaize connections, works the best.
'''
