class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
#         N = len(nums)
#         for i in range(N):
#             if nums[i] >= target:
#                 return i
            
#         return N
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
                

            