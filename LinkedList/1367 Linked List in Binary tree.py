# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return (self.isContinuesPath(head,root) or self.isSubPath(head,root.left) or 
        self.isSubPath(head,root.right))
    def isContinuesPath(self,head:Optional[ListNode],root:Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return (head.val == root.val and 
        (self.isContinuesPath(head.next,root.left) or 
        self.isContinuesPath(head.next,root.right)))

'''
isContinues() is important in this problem. It takes the head and root.
1. Check whether the values of head and root are equal.
2. it also checks that the next element of the head is equal to the next right or left root node.
2.1 It calls again and again and compares the head and present root value
3. If both conditions are equal then it returns true.
'''
