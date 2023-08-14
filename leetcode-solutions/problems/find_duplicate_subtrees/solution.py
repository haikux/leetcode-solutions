# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)

        def dfs(node):
            if not node:
                return "#"
            # Serialize the tree for hashing purposes
            st = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            # Avoid capturing duplicate entries
            if len(subtrees[st]) == 1:
                res.append(node)
            subtrees[st].append(st)
            return st
        res = []
        dfs(root)
        return res

