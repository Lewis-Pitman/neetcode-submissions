class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Use a dummy node to simplify edge cases at the head
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # 1. Check if there are k nodes left to reverse
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            
            # 2. Reverse the group
            # We isolate the group by temporarily cutting it off
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 3. Update the links
            # After reversal, 'kth' is the new head of the group
            # and 'group_prev.next' (the old head) is now the tail
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr