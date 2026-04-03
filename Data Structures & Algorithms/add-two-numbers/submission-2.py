# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        l1_curr = l1
        l2_curr = l2

        result_head = None
        result_prev = None
        carry_over = 0

        while l1_curr is not None or l2_curr is not None:
            l1_val = l1_curr.val if l1_curr is not None else 0
            l2_val = l2_curr.val if l2_curr is not None else 0

            val_sum = l1_val + l2_val + carry_over
            carry_over = val_sum // 10
            remainder = val_sum % 10

            new_node = ListNode(val=remainder)

            if result_prev != None:
                result_prev.next = new_node
            else:
                result_head = new_node
            
            result_prev = new_node

            if l1_curr is not None:
                l1_curr = l1_curr.next

            if l2_curr is not None:
                l2_curr = l2_curr.next
        
        if carry_over > 0:
            new_node = ListNode(val=carry_over)

            if result_prev != None:
                result_prev.next = new_node
            else:
                result_head = new_node
            
            result_prev = new_node
        
        return result_head
        