# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        res = list()
        que = deque([root])
        while que:
            _len = len(que)
            curr_res = list()
            for _ in range(_len):
                curr_node = que.popleft()
                curr_res.append(curr_node.val)

                if curr_node.left:
                    que.append(curr_node.left)
                if curr_node.right:
                    que.append(curr_node.right)
            
            res.append(curr_res)
        return res