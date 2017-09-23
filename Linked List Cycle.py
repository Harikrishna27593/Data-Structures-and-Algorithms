# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr1=head
        ptr2=head
        
        while ptr1 is not None and ptr1.next is not None:
            ptr1=ptr1.next.next
            ptr2=ptr2.next
            if(ptr1==ptr2):
                return True
        
        return False

