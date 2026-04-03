# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Output Breadth first search as a string
    # None is represented as 😎 and delimited by ,
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        tree_vals = []
        de = deque([root])

        while de:
            curr = de.pop()

            if curr is None:
                tree_vals.append("😎")
                tree_vals.append(",")
                continue
            
            tree_vals.append(str(curr.val))
            tree_vals.append(",")

            de.appendleft(curr.left)
            de.appendleft(curr.right)
        
        return "".join(tree_vals)

        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "😎":
            return None
        
        values = data.split(",")
        data_ptr = 1

        root = TreeNode(int(values[0]))
        children_unassigned = deque([root])

        while children_unassigned and data_ptr < len(values):
            curr = children_unassigned.pop()

            # Left
            if data_ptr < len(values) and values[data_ptr] != "😎":
                left_node = TreeNode(int(values[data_ptr]))
                curr.left = left_node
                children_unassigned.appendleft(left_node)
            data_ptr += 1

            # Right
            if data_ptr < len(values) and values[data_ptr] != "😎":
                right_node = TreeNode(int(values[data_ptr]))
                curr.right = right_node
                children_unassigned.appendleft(right_node)
            data_ptr += 1

        return root
