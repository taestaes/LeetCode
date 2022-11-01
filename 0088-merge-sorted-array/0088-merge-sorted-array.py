class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        
        while i<m+n and j < n:
            if nums1[i] > nums2[j]:
                nums1[i+1:m+n] = nums1[i:m+n-1]
                nums1[i] = nums2[j]
                j = j+1
                i = i+1
            else:
                i = i+1
                
        nums1[j+m:m+n] = nums2[j:n]
        
        return nums1