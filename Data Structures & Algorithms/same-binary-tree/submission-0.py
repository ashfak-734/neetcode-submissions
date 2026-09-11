# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_p  = []
        list_q  = []

        def traverse_p(p):
            if not p:
                list_p.append(None)
                return 
            list_p.append(p.val)

            traverse_p(p.left)
            traverse_p(p.right)

        def traverse_q(q):
            if not q:
                list_q.append(None)
                return 
            list_q.append(q.val)

            traverse_q(q.left)
            traverse_q(q.right)

        traverse_p(p)
        traverse_q(q)

        if list_p == list_q:
            return True 
        else:
            return False

        