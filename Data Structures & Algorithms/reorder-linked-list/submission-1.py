# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)
      
        fast = slow = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        while curr:
            t = curr.next 
            curr.next = prev
            prev = curr
            curr = t
        
        slow.next = None

        curr1,curr2 = head,prev

        while curr2: #4 #6
            t1 = curr1.next  # none
            t2 = curr2.next #none
            curr1.next = curr2
            curr2.next = t1
            curr1 = t1
            curr2 = t2





        