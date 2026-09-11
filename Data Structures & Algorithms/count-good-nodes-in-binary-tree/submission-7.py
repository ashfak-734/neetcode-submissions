# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        R = [root]
        def dfs(root,low=float("-inf")):
            if not root:
                return 

            if root.val >= low:
                count[0] += 1

            low = max(low,root.val)

            dfs(root.left,low)
            dfs(root.right,low)

        dfs(root)
        return count[0]

            
        