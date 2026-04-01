# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        output = list()
        queue = deque([root])

        while queue:
            _len = len(queue)
            for i in range(_len):
                curr_node = queue.popleft()
                if i == _len - 1:
                    output.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
                
        return output
        