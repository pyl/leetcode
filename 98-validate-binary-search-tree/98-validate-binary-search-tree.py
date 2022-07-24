# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lm, rm):
            if root == None:
                return True
            if root.val <= lm or root.val >= rm:
                return False
            return dfs(root.left, min(lm, root.val), min(rm, root.val)) and dfs(root.right, max(lm, root.val), max(rm, root.val))
        return dfs(root, float("-inf"), float("inf"))