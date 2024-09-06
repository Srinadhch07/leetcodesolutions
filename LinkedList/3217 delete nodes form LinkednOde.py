# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        modified_num = set(nums)
        current = dummy
        while current.next:
            if current.next.val in modified_num:
                current.next = current.next.next
            else:
                current = current.next
            
        return dummy.next
        
