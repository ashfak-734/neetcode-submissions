"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        o_to_n = {}
        def clone(node):
             
            if node in o_to_n:
                return o_to_n[node] 

            copy = Node(node.val)
            o_to_n[node] = copy 

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy


        return clone(node) if node else None
        