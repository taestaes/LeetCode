class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        N = len(nums)
        for i in range(N):
            if nums[i] >= target:
                return i
            
        return N
            