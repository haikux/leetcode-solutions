# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Idea 1 - Iterative BFS
        """
        q = deque()
        if root:
            q.append(root)
        
        result = []
        level = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if level % 2 == 0:
                tmp = tmp[::-1]
            result.append(tmp)
        
        return result
    """

        # Idea 2 - DFS
        result = []
        if not root:
            return result
        def dfs(root, level):
            if len(result) == level:
                result.append(deque([]))
            
            if level % 2 == 0:
                result[level].append(root.val)
            else:
                result[level].appendleft(root.val)
            
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)
        return result
            
        