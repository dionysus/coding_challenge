'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
Medium
'''

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:

    def helper(root):
      # check root
      if not root:
        return True, None, None
      
      # check child nodes
      if root.left is not None and root.left.val >= root.val:
        return False, None, None
      if root.right is not None and root.right.val <= root.val:
        return False, None, None

      # check left tree
      valid_left, min_left, max_left = helper(root.left)
      if not valid_left:
        return False, None, None
      elif min_left is None:
        min_left = root.val
      elif max_left >= root.val:
        return False, None, None

      # check right tree
      valid_right, min_right, max_right = helper(root.right)

      if not valid_right:
        return False, None, None
      elif max_right is None:
        max_right = root.val
      elif min_right <= root.val:
        return False, None, None

      # combine left and right
      return True, min_left, max_right
    
    valid, min_left, max_right = helper(root)
    return valid