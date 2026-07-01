# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        addition = res
        coma = 0
        previous = None
        while l1 != None and l2 != None:
            num = l1.val + l2.val
            addition.val = (num + coma) % 10
            addition.next = ListNode()
            previous = addition
            addition = addition.next
            if num+coma >= 10:
                coma =1
            else:
                coma = 0
            l1 = l1.next
            l2 = l2.next
        
        if l2 != None:
            l1 = l2
        while l1 != None:
            num = l1.val
            addition.val = (num+coma) % 10
            addition.next = ListNode()
            previous = addition
            addition = addition.next
            if num+coma >= 10:
                coma = 1
            else:
                coma = 0
            l1 = l1.next
        if coma == 1:
            addition.val = 1
        elif previous != None:
            previous.next = None
        

        return res
