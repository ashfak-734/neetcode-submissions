# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = 0

        def dfs(root):
            nonlocal LCA

            if not root:
                return 

            LCA = root

            if root.val > p.val and root.val > q.val:
                dfs(root.left)
            elif root.val < p.val and root.val < q.val:
                dfs(root.right)
            else:
                return  

        dfs(root)

        return LCA



        