# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Queue is structured as a pair of (node, max val above node)
        de = deque([(root, root.val)])
        good_nodes = 0

        while de:
            curr = de.pop()
            curr_node = curr[0]
            max_val_above = curr[1]

            if curr_node is not None:
                if curr_node.val >= max_val_above:
                    good_nodes += 1
                
                de.appendleft((curr_node.left, max(max_val_above, curr_node.val)))
                de.appendleft((curr_node.right, max(max_val_above, curr_node.val)))

        return good_nodes