# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is not None:
            return self.isSymmetric_helper(root.left, root.right)
        else:
            return True

    def isSymmetric_helper(self, left: TreeNode, right: TreeNode):

        if (left and not right) or (right and not left):
            return False

        if not left and not right:
            return True

        if left.val != right.val:
            return False

        return self.isSymmetric_helper(left.left, right.right) and \
               self.isSymmetric_helper(left.right, right.left)
