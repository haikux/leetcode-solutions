# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        # Idea 1 - Usual BFS, just reverse the list in the end
        q = deque()
        result = []
        if root:
            q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                n = q.popleft()
                tmp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            result.append(tmp)
        
        
        return result[::-1]
        """

        # Idea 2 - Use recursive DFS 
        result = []
        if not root:
            return result
        
        def dfs(root, level):
            if len(result) == level:
                result.append([])
            
            result[level].append(root.val)

            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        
        dfs(root, 0)
        return result[::-1]
            
            
            
            

        