# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
    
    # Loop until both lists are empty AND carry is 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
        
        # Calculate total sum for this digit
            total = val1 + val2 + carry
            carry = total // 10
        
        # Create new node for the digit
            current.next = ListNode(total % 10)
            current = current.next
        
        # Move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next