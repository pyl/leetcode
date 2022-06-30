# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(node):
            if node == None:
                return 0
            hl = dfs(node.left)
            hr = dfs(node.right)
            if abs(hr - hl) > 1:
                res[0] = False
            return 1 + max(hl, hr)
        dfs(root)
        return res[0]