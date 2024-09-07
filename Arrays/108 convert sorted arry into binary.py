# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left,right):
            if left > right:
                return None
            middle = (left+right)//2

            return TreeNode(nums[middle],build(left,middle-1),build(middle+1,right))
        return build(0,len(nums))
        
