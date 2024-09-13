# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lefttree = root.left
        righttree= root.right
        return self.isSym(lefttree,righttree)
    def isSym(self,lefttree,righttree):
        if lefttree is None and righttree is None:
            return True
        elif lefttree is None or righttree is None:
            return False
        elif lefttree.val!=righttree.val:
            return False
        else:
            return self.isSym(lefttree.left,righttree.right) and self.isSym(lefttree.right,righttree.left)
