# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        def dfs(root, curr_sum=0):
            if root is None: return 0

            curr_sum = curr_sum * 10 + root.val
            
            if root.left is None and root.right is None: return curr_sum

            left = dfs(root.left, curr_sum)
            right = dfs(root.right, curr_sum)
            return left + right

        return dfs(root, 0)