# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return root
        
        # postorder traversal
        self.invertTree(root.right)
        self.invertTree(root.left)

        root.right, root.left = root.left, root.right #swap the left and right child

        return root
        