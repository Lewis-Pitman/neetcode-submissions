# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen_nodes = set()
        current_node = head

        while current_node.next != None:
            if current_node in seen_nodes:
                return True
            seen_nodes.add(current_node)
            current_node = current_node.next 
        
        return False