class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        one_pointer = 0
        N = len(nums)
        
        for i in range(N):
            if nums[i] == 0:
                zero_pointer += 1
                
            elif nums[i] == 1:
                one_pointer += 1
                
        for i in range(N): 
            if i<zero_pointer:
                nums[i] = 0
            elif i<zero_pointer+one_pointer:
                nums[i] = 1
            else:
                nums[i] = 2
                
        return nums