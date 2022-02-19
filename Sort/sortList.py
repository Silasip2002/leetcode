# Leetcode 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check the base case
        if head is None or head.next is None:
             return head

        # base setting of mergetSort
        dummy = ListNode()
        dummy.next = head
        fast = dummy  # the first pointer is for looping
        slow = dummy  # the slow pointer is for determine the pivot

        if fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        head2 = ListNode()
        head2 = slow.next
        slow.next = None  # remember seperate two head

        return self.merge(head, head2)

    def merge(self, head: Optional[ListNode],head2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            res = dummy.next

            if head.val < head2.val:
                res.next = head
                res = res.next 
                head = head.next
            else :
                res.next = head2
                res = res.next
                head2 = head2.next

            # check the reminder and added it to the res 
            if head1:
                res.next = head1
            if head2:
                res.next = head2
            # return the ans
            print ("dummy",dummy.next)
            return dummy.next 

        
        
    
    
        
        
