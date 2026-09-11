# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = set()

        def bfs(root):
            if not root:
                return 

            bfs(root.left)
            s.add(root.val)
            bfs(root.right)
            s.add(root.val)

        bfs(root)

        my_list = list(s)
        return my_list[k-1]