class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node that points to head
        # This handles the edge case of removing the head node itself
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # 2. Advance 'fast' so there are n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next

        # 3. Move both until fast reaches the end
        # slow will stop exactly one node BEFORE the target
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # 4. Delete the node by skipping it
        # slow.next is the node to be removed
        slow.next = slow.next.next

        # 5. Return the 'real' head
        return dummy.next