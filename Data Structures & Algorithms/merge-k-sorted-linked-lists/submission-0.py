# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If no lists given
        if not lists:
            return None

        pointers = lists.copy()

        dummy = ListNode()
        curr = dummy

        while not all(pointer is None for pointer in pointers):
            min_node = None
            min_node_index = None

            # Loop through all current pointers to find smallest val
            for index, pointer in enumerate(pointers):
                min_node_val = min_node.val if min_node is not None else float("inf")
                val = pointer.val if pointer is not None else float("inf")
                
                if val < min_node_val:
                    min_node = pointer
                    min_node_index = index
            
            if min_node_index is not None and pointers[min_node_index] is not None:
                pointers[min_node_index] = pointers[min_node_index].next

            curr.next = min_node
            curr = min_node

        return dummy.next