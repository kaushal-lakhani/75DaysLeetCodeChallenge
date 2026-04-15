# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = [(root,0)]
        md = 0
        while q:
            n, d = q.pop()
            d += 1
            if n:
                if n.left:
                    q.append((n.left,d))
                if n.right:
                    q.append((n.right,d))
                md = max(md, d)
        return md