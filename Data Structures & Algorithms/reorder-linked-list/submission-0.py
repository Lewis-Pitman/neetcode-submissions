class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        mid = self.middleNode(head)

        # Reverse the right side of the list for easy traversal
        head2 = self.reverseList(mid.next)

        # Detatch mid from the reversed list
        mid.next = None

        # Two pointers, one at head, other at mid.next
        p1_curr = head
        p2_curr = head2

        # The loop condition needs to ensure p2_curr exists to be inserted
        while p1_curr != None and p2_curr != None:
            # 1. Save the actual next nodes before we break the links
            p1_next = p1_curr.next
            p2_next = p2_curr.next

            # 2. Insert p2_curr in between p1_curr and p1_next
            p1_curr.next = p2_curr
            p2_curr.next = p1_next

            # 3. Move both pointers along to the saved "next" positions
            p1_curr = p1_next
            p2_curr = p2_next

    def middleNode(self, head: Optional[ListNode]) -> ListNode:
        # Return the middle node of a linked list
        curr = head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next

        curr = head

        for i in range(count // 2):
            curr = curr.next

        return curr

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        # Reverse a linked list in-place
        if head is None:
            return None

        prev = None
        curr = head

        while curr != None:
            # Save next node
            temp = curr.next

            # Replace next node with previous node
            curr.next = prev

            # Set current node to saved node and prev to one before
            prev = curr
            curr = temp

        return prev