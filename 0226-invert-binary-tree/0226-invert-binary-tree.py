# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]

        while q:
            n = q.pop(0)
            if n and n.left:
                q.append(n.left)
            if n and n.right:
                q.append(n.right)
            if n:
                n.left, n.right = n.right, n.left
        
        return root