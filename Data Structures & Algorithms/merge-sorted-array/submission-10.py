class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
            j = m + i - 1
            while j >= 0 and nums1[j] > nums1[j + 1]:
                temp = nums1[j + 1]
                nums1[j + 1] = nums1[j]
                nums1[j] = temp
                j -= 1