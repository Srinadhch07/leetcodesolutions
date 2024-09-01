class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        com_list = nums1[:m]+nums2
        com_list.sort()
        for i in range(len(nums1)):
            nums1[i]=com_list[i]
        
        
