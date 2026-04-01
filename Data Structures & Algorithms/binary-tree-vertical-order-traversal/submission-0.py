# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        result = list()
        queue =deque([(root, 0)])
        hashMap = defaultdict(list)
        while queue:
            _len = len(queue)

			# process the current node and store in hashmap
            for _ in range(_len):
                curr_node, column = queue.popleft()
                hashMap[column].append(curr_node.val)
                if curr_node.left: 
                    queue.append((curr_node.left, column - 1))
                if curr_node.right:
                    queue.append((curr_node.right, column + 1))
        sorted_columns = list(hashMap.keys())
        sorted_columns.sort()
        for col in sorted_columns:
            result.append(hashMap[col])
        return result