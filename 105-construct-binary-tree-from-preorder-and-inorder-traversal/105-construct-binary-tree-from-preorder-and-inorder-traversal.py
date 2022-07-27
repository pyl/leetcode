# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - process both before.
        # inorder - process left, then parent, then right
        # postorder - process parent, then left, then right
        # inorder goes from left to right. thats the whole point of it.
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = preorder[0]
        newNode = TreeNode(root)
        mid = inorder.index(root)
        newNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        newNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return newNode