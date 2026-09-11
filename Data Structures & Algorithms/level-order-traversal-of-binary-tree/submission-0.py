# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q= deque() 
        if root is None:
            return [] 
        q.append(root)
        result = []  #[[1],[2,3],[4,5,6,7]]
        
        while q:  #[]
            level = []   #[4,5,6,7]
            n = len(q) #4
            for _ in range(n): #4
                node = q.popleft()  
                level.append(node.val)  

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result 
                
        
        


        