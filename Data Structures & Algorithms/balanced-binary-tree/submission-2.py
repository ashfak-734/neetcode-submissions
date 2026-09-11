# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalanced(root: Optional[TreeNode]) -> bool:
            if root is None:
                return 0 

            left_h = isBalanced(root.left)
            if left_h is False:
                return False

            right_h = isBalanced(root.right)
            if right_h is False:
                return False

            if abs(left_h - right_h) > 1:
                return False

            return max(left_h,right_h) + 1
        
        result = isBalanced(root)
        
        return result is not False

    

        