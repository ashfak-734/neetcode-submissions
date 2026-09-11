# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = [root.val]
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            left = max(0,left)
            right = max(0,right)

            maxx[0] = max(maxx[0],root.val+left+right)

            return max(left,right)+root.val

        dfs(root)
        return maxx[0]





            
        