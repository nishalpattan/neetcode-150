# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(p, q):
            # base case
            if p is None and q is None: return True
            # edge case
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False

            left_subtree = preorder(p.left, q.left)
            right_subtree = preorder(p.right, q.right)
            return left_subtree and right_subtree

        return preorder(p, q)
