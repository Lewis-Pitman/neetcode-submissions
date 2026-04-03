# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        de = deque([root])

        while de:
            curr = de.popleft()

            if curr is not None:
                de.append(curr.left)
                de.append(curr.right)

            if self.same(curr, subRoot):
                return True
        
        return False


    def same(self, root_a: Optional[TreeNode], root_b: Optional[TreeNode]) -> bool:
        if root_a is None and root_b is None:
            return True

        if root_a is None or root_b is None:
            return False

        if root_a.val != root_b.val:
            return False

        return self.same(root_a.left, root_b.left) and self.same(root_a.right, root_b.right)
        

        

        