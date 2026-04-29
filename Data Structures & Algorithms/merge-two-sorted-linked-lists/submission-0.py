# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_list = ListNode(0) # 0 => None || 0 > 1 > None || 0 -> 1 -> 2 -> None
        head = new_list # 0 => None || 
        while list1 and list2: # 1 > 2 > 4 and 1 -> 3 -> 5 || 2 > 4 and  1 > 3 > 5
            list1_val = list1.val # 1 || 2
            list2_val = list2.val # 1 || 1
            if list1_val <= list2_val: # 1<=1 || 2 <= 1
                new_list.next = ListNode(list1_val) 
                list1 = list1.next # 2 > 4
            else:
                new_list.next = ListNode(list2_val) 
                list2 = list2.next # 3 > 5
            new_list = new_list.next # 1 > None
        if list1 and not list2:
            new_list.next = list1
        if list2 and not list1:
            new_list.next = list2
        return head.next
        

