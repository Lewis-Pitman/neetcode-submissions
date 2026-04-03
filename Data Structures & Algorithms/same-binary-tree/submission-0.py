# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_vals = []
        q_vals = []

        p_queue = [p]
        q_queue = [q]

        while p_queue or q_queue:
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)

            if p_curr is not None:
                p_vals.append(p_curr.val)
                p_queue.append(p_curr.left)
                p_queue.append(p_curr.right)

            if q_curr is not None:
                q_vals.append(q_curr.val)
                q_queue.append(q_curr.left)
                q_queue.append(q_curr.right)
            
            if p_vals != q_vals:
                return False

        return p_vals == q_vals