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
        dic = {}

        curr = head

        while curr:
            dic[curr] = Node(0)
            curr = curr.next

        curr1 = head

        while curr1:
            dic[curr1].val = curr1.val
            dic[curr1].next = dic[curr1.next] if curr1.next else None
            dic[curr1].random = dic[curr1.random] if curr1.random else None
            curr1 = curr1.next

        return dic[head] if head else None
        

            

        