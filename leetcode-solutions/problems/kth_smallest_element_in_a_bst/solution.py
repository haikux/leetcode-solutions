# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root

        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        
        """
        # Recursive
        count = [0]
        result = [0]
        def dfs(root, k):
            if not root:
                return [0]
            
            dfs(root.left, k)

            count[0] += 1
            if count[0] == k:
                result[0] = root.val
                return result

            dfs(root.right, k)

            return result
        dfs(root, k)
        return result[0]
        """
        