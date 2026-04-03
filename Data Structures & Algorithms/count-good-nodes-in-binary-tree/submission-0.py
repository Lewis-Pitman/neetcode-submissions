# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_node_count = 0

        # max_node_val represents the highest val in the path from root to node
        def checkNode(node: TreeNode, max_node_val: int):
            if node is not None:
                if node.val >= max_node_val:
                    self.good_node_count += 1
                
                checkNode(node.left, max(max_node_val, node.val))
                checkNode(node.right, max(max_node_val, node.val))
        
        checkNode(root, root.val)

        return self.good_node_count