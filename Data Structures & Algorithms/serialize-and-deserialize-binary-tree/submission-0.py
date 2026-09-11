# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("null")
                return 
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        count = 0

        def dfs():
            nonlocal count
            if data[count] == "null":
                count+=1
                return 

            root = TreeNode(int(data[count]))
            count += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()

