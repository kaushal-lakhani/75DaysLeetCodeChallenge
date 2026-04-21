# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root,0)]
        res = defaultdict(list)

        while q:
            n = q.pop()
            if n[0]:
                # print(n[0].val)
                res[n[1]].append(n[0].val)
            if n[0] and n[0].right:
                q.append((n[0].right,n[1]+1))
            if n[0] and n[0].left:
                q.append((n[0].left,n[1]+1))
        
        return [res[x] for x in range(0,len(res))]