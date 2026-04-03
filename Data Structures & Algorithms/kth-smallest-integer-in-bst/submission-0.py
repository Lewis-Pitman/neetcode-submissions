# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = None

        def createStack(curr):
            if curr is not None:
                createStack(curr.right)
                stack.append(curr)
                createStack(curr.left)

        createStack(root)

        for i in range(k):
            if stack is not None:
                curr = stack.pop()
        
        return curr.val