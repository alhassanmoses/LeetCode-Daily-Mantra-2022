# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

# Definition for a binary tree node.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        left = self.depthCount(root, 0)
        right = self.depthCount(root, 0)
        
        return max(left, right)
        
    def depthCount(self, newRoot, current_count):
        
        if newRoot is None:
            return current_count
        
        left_branch_depth = self.depthCount(newRoot.left, current_count + 1)
        right_branch_depth = self.depthCount(newRoot.right, current_count +1)
        
        return max(left_branch_depth, right_branch_depth)