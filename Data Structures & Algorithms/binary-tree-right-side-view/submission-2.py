# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ends = []

        if not root:
            return []

        queue.append(root)

        level = 0
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if i == n - 1:
                    ends.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        
        return ends