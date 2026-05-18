# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val, None]
        q = [(root,0)]

        while q:
            n,l = q.pop(0)
            if n and n.left:
                q.append((n.left,l+1))
            if n and n.right:
                q.append((n.right,l+1))

            if res[l] == None:
                res.append(None)
            res[l]=n.val
        return res[:-1]