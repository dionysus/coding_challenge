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
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

bool hasPathSum(struct TreeNode* root, int sum){
  if (root == NULL) return false;
  if ((root->left == NULL) && (root->right == NULL)){
    return sum - root->val == 0;
  }
  return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
}

