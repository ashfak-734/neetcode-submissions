# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string =  []

        def dfs(root):
            if not root:
                string.append("null")
                return 

            string.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(string)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data = data.split(",")

        count = 0

        def dfs(data):
            nonlocal count
            if data[count] == "null":
                count += 1
                return 
            
            root = TreeNode(int(data[count]))
            count += 1
            root.left = dfs(data)
            root.right = dfs(data)

            return root
        
        return dfs(data)
        
        
            


