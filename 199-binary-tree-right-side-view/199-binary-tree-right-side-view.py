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
        s = []
        s.append(root)
        res = []
        while len(s) > 0:
            res.append(s[-1].val)
            new = []
            for x in s:
                if x.left:
                    new.append(x.left)
                if x.right:
                    new.append(x.right)
            s = new
        return res
                