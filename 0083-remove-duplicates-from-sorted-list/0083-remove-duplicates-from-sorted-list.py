# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Return immediately if list is empty
        if not head:
            return head
        
        current = head
        
        # Traverse until the end of the list
        while current and current.next:
            # Skip the next node if it has a duplicate value
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move forward only if no duplicate was found
                current = current.next
                
        return head
