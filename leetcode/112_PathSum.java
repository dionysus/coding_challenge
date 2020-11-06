/**
 * 112. Path Sum 
 * Difficulty: Easy
 * URL: https://leetcode.com/problems/path-sum/
 * 
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
 * such that adding up all the values along the path equals the given sum.
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  public boolean hasPathSum(TreeNode root, int sum) {
    // base case
    if (root == null){
      return false;
    }

    if ((root.left == null) & (root.right == null)) {
      return sum - root.val == 0;
    }

    // recursive case 
    return (hasPathSum(root.left, sum - root.val) || 
            hasPathSum(root.right, sum - root.val));
  }
}