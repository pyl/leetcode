# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, res):
        if node == None:
            return
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        
    

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        print(res)
        return res
        