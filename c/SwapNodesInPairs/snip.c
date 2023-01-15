/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* current = dummy;
    
    while(current->next && current->next->next)
    {
        struct ListNode* first_node = current->next;
        struct ListNode* second_node = current->next->next;
        first_node->next = second_node->next;
        current->next = second_node;
        current->next->next = first_node;
        current = current->next->next;
    }

    return dummy->next;

}
