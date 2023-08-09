# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        if root:
            dq.append(root)
        res = []

        while dq:
            val = []
            for i in range(len(dq)):
                n = dq.popleft()
                val.append(n.val)

                if n.left:
                    dq.append(n.left)
                if n.right:
                    dq.append(n.right)
            res.append(val)
        return res

            
