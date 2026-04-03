# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")

        if root is None:
            return 0
        
        def maxSum(curr: Optional[TreeNode]) -> int:
            if curr is None:
                return 0
            
            max_sum_left = maxSum(curr.left)
            max_sum_right = maxSum(curr.right)
            
            max_with_left = max_sum_left + curr.val
            max_with_right = max_sum_right + curr.val
            max_with_both = max_sum_left + max_sum_right + curr.val

            max_sum = max(max_with_left, max_with_right, curr.val)
            self.result = max(self.result, max_sum, max_with_both)

            return max_sum

        maxSum(root)

        return self.result
