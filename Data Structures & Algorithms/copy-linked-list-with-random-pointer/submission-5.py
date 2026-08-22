"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        org = head
        my_dic = {}

        while org:
            my_dic[org] = Node(org.val)
            org = org.next
        
        org = head

        while org:
            new_node = my_dic[org]
            new_node.next = my_dic[org.next] if org.next else None
            new_node.random = my_dic[org.random] if org.random else None

            org = org.next

          
        return my_dic[head] if head else None

            
              
        