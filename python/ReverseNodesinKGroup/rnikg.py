# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        # Edge case: if k is 1 or 0, return the original list
        if k <= 1:
            return head

        # Create a dummy node to serve as the new head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Iterate through the list in steps of k
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            # Reverse the sublist [prev.next, tail]
            head = prev.next
            for i in range(k - 1):
                temp = head.next
                head.next = temp.next
                temp.next = prev.next
                prev.next = temp

            # Update prev to the tail of the reversed sublist
            prev = head
            head = head.next

        return dummy.next

