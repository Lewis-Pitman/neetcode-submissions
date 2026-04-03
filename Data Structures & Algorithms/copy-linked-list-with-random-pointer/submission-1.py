"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        old_node_to_new_node = {}

        curr = head

        while curr != None:
            old_node_to_new_node[curr] = Node(curr.val)
            curr = curr.next

        for old_node, new_node in zip(old_node_to_new_node.keys(), old_node_to_new_node.values()):
            if old_node.next is None:
                new_node.next = None
            else:
                new_node.next = old_node_to_new_node[old_node.next]
            
            if old_node.random is None:
                new_node.random = None
            else:
                new_node.random = old_node_to_new_node[old_node.random]
        
        return old_node_to_new_node[head]
