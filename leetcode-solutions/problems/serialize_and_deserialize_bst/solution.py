# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)            
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        new_data = data.split(",")
        self.idx = 0
        def dfs():
            if new_data[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(new_data[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans