# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areEqual(root1, root2):
            if bool(root1) != bool(root2):
                return False
            if root1 == None and root2 == None:
                return True
            return root1.val == root2.val and areEqual(root1.left, root2.left) and areEqual(root1.right, root2.right)
        def dfs(root):
            if not root:
                return False
            if areEqual(root, subRoot):
                return True
            else:
                return dfs(root.left) or dfs(root.right)
        return dfs(root)