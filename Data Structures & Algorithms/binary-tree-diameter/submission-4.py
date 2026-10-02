# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        maxWithRoot = 0
        if not root.left:
            maxWithRoot = 1 + self.longest(root.right)
            return max(maxWithRoot, self.diameterOfBinaryTree(root.right))
        if not root.right:
            maxWithRoot = 1 + self.longest(root.left)
            return max(maxWithRoot, self.diameterOfBinaryTree(root.left))
        maxWithRoot = 2 + self.longest(root.left) + self.longest(root.right)
        return max(maxWithRoot, self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right))


    def longest(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        if not root.left:
            return 1 + self.longest(root.right)
        if not root.right:
            return 1 + self.longest(root.left)
        return 1 + max(self.longest(root.left), self.longest(root.right))