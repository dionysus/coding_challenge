# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None or root.val is None:
            return 0

        elif root.left is None and root.right is None:
            return 1

        else:
            depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            return depth
