# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        result = []

        def solve(root, depth):
            if root is not None:
                if len(result) == depth:
                    result.append(root.val)

                solve(root.right, depth + 1)
                solve(root.left, depth + 1)

        solve(root, 0)
        
        return result

    

