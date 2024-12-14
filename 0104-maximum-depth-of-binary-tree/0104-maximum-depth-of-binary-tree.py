# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        max_depth = max(left_max_depth, right_max_depth) + 1

        return max_depth
