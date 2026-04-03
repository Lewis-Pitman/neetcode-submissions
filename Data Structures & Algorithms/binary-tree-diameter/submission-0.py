# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        
        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            self.best = max(self.best, left_height + right_height)

            return 1 + max(left_height, right_height)

        get_height(root)
        return self.best
