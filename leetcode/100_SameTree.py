# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # Base Case
        if p is None and q is None:
            return True

        if (p is None and q is not None) or (q is None and p is not None):
            return False

        if p.val != q.val:
            return False

        # Recursion
        else:
            # if not (self.isSameTree(p.left, q.left) and self.isSameTree(
            #         p.right, q.right)):
            #     return False
            #
            # return True

            return self.isSameTree(p.left, q.left) and self.isSameTree(
                    p.right, q.right)
