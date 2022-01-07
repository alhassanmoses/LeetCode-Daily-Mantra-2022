# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        result = []
        self.traverse(root, result)
        
        return result
        
        
    def traverse(self, node, values):
        
        if node is None:
            return
        
        if node.left is not None:
            self.traverse(node.left, values)
            
        values.append(node.val)
            
        if node.right is not None:
            self.traverse(node.right, values)

        return
