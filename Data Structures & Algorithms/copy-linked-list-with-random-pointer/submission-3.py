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
        
        for node in my_dic:
            next_node = node.next
            random = node.random

            my_dic[node].next = my_dic[next_node] if next_node else None
            my_dic[node].random = my_dic[random] if random else None

      

        return my_dic[head] if head else None

            
              
        