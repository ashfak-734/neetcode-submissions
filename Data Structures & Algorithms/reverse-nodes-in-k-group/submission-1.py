# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        D = ListNode(next=head)
        groupprev = D

        while True:
            kth = self.kth_node(k,groupprev)

            if kth is None:
                break

            groupnext = kth.next
    

            #reverse the group

            prev,curr = kth.next,groupprev.next    
            while curr != groupnext:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t

            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp 

        return D.next


    def kth_node(slef,k,curr):
            while curr and k>0:
                curr = curr.next
                k -= 1 

            return curr



        
        