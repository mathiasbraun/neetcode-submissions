# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Search for the node subRoot in root.
        # subRoot can occur multiple times!
        # So go through entire root tree and collect
        # occurrences of subRoot
        q = [root]
        occ = []
        while q:
            cur = q.pop(0)
            if cur.val == subRoot.val:
                occ.append(cur)
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        if not occ:
            return False
        
        while occ:
            cur = occ.pop(0)
            if self.isSameTree(cur, subRoot):
                return True

        return False


    
    # Imported from my solution for "Is same tree"
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        
        qp = [p]
        qq = [q]

        while qp and qq:
            np = qp.pop(0)
            nq = qq.pop(0)
            if (np.val != nq.val or (np.left and not nq.left)
                                 or (np.right and not nq.right)
                                 or (not np.left and nq.left)
                                 or (not np.right and nq.right)):
                return False

            if np.left and nq.left:
                qp.append(np.left)
                qq.append(nq.left)
            if np.right and nq.right:
                qp.append(np.right)
                qq.append(nq.right)

        if (qp and not qq) or (not qp and qq):
            return False

        return True