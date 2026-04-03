# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Early returns for invalid parameters
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Find which list starts with the smaller val to start off
        # Always make list1 start with the smaller val
        if list2.val < list1.val:
            list1, list2 = list2, list1

        ls1_curr = list1
        ls2_curr = list2

        # Loop through list 1 until we hit the end OR list 2 is exhausted
        while ls1_curr.next is not None and ls2_curr is not None:
            # If ls2 smaller than the NEXT node in ls1:
            if ls2_curr.val < ls1_curr.next.val:
                # Save ls1 current node next in temp
                temp = ls1_curr.next

                # Change current node next to ls2 current node
                ls1_curr.next = ls2_curr

                # Traverse ls2 until no longer smaller than the saved temp
                while ls2_curr.next is not None and ls2_curr.next.val < temp.val:
                    ls2_curr = ls2_curr.next

                # Save the remainder of list 2 before re-linking
                next_ls2_node = ls2_curr.next
                
                # Link the end of this ls2 segment back to list 1
                ls2_curr.next = temp
                
                # Move ls2 pointer to the start of its remaining nodes
                ls2_curr = next_ls2_node
            
            # Move through list 1
            ls1_curr = ls1_curr.next
        
        # If list 1 ended but list 2 still has nodes, attach them to the tail
        if ls2_curr is not None:
            ls1_curr.next = ls2_curr
            
        return list1