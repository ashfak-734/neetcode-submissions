# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bfs(root,max=float("inf"),min=float("-inf")):
            if not root:
                return True 

            if root.val >= max or root.val<=min:
                return False

            return bfs(root.left,root.val,min) and bfs(root.right,max,root.val)

        return bfs(root)

           



            

           

        

        