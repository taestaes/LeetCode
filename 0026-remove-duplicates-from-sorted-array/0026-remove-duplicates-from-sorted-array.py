class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        N=len(nums)
        i=0
        for j in range(0,N):
            if nums[i] < nums[j]:
                nums[i+1] = nums[j]
                i = i+1

        return i+1