# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def nodeValid(
            node: Optional[TreeNode], 
            minimum: float = float("-inf"), 
            maximum: float = float("inf")
            ) -> bool:
            if node is None:
                return True
            
            in_range = node.val > minimum and node.val < maximum

            return (
                in_range 
                and nodeValid(node.left, minimum, node.val)
                and nodeValid(node.right, node.val, maximum)
                )
        
        return nodeValid(root)
