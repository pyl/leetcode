# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        basedNum = [1]
        res = [None]
        def dfs(root):
            if root.left:
                dfs(root.left)
            if basedNum[0] == k:
                res[0] = root.val
            basedNum[0] += 1
            if root.right:
                dfs(root.right)
        dfs(root)
        return res[0]