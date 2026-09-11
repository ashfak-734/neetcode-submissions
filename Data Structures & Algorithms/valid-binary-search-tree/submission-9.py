# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,high=float("inf"),low= float("-inf")):
            if not root:
                return True 

            if root.val >= high:
                return False

            if root.val <= low:
                return False 

            return dfs(root.left,root.val,low) and dfs(root.right,high,root.val)


        return dfs(root)


            
        