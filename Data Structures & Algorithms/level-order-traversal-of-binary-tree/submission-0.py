from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)  # This is the "goal" for the current level
            curr_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)
                
                # Only add children if they actually exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(curr_level)

        return result