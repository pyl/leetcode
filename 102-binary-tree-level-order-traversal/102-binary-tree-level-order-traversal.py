# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        s = []
        s.append(root)
        
        res = []
        
        while len(s) > 0:
            res.append([x.val for x in s])
            new = []
            for x in s:
                if x.left:
                    new.append(x.left)
                if x.right:
                    new.append(x.right)
            s = new
        return res
                
                