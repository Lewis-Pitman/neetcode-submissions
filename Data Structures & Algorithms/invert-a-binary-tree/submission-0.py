# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Breadth first search

        queue = [root]

        while queue:
            parent = queue.pop(0)

            if parent is not None:
                queue.append(parent.left)
                queue.append(parent.right)
                
                parent.left, parent.right = parent.right, parent.left
        
        return root
