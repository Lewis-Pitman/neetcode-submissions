# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        currentRow = [root]
        count = 0

        while not all(node is None for node in currentRow):
            currentRow = self.checkRow(currentRow)
            count += 1

        return count

    def checkRow(self, row: list[Optional[TreeNode]]) -> list[Optional[TreeNode]]:
        # Check the current row and return the next row
        newRow = []

        for node in row:
            if node is not None:
                newRow.append(node.left)
                newRow.append(node.right)

        return newRow