# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        elif (not s and t) or (s and not t):
            return False

        else:
            if s.val == t.val:
                if self.isSubtreeHelper(s.left, t.left) and \
                        self.isSubtreeHelper(s.right, t.right):
                    return True

            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtreeHelper(self, s: TreeNode, t: TreeNode) -> bool:

        if not s and not t:
            return True

        elif (not s and t) or (s and not t):
            return False

        else:
            if s.val == t.val:
                return self.isSubtreeHelper(s.left, t.left) and \
                        self.isSubtreeHelper(s.right, t.right)

