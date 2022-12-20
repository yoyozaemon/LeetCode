# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_node_a = l1
        list_node_b = l2
        temp_node = list_node_c = ListNode(0)
        while list_node_a or list_node_b:
            a = b = 0  
            if not list_node_a:
                list_node_a = ListNode(0)
            a = list_node_a.val
            if not list_node_b:
                list_node_b = ListNode(0)
            b = list_node_b.val
            temp_add = a + b + temp_node.val
            temp_node.val = temp_add % 10
            if temp_add // 10 == 1:
                 temp_node.next = ListNode(1)
            else:
                if list_node_a.next or list_node_b.next:
                    temp_node.next = ListNode(0)  
                
            list_node_a = list_node_a.next
            list_node_b = list_node_b.next
            temp_node = temp_node.next
        return list_node_c
        
