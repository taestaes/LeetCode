class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        N = len(digits)
        last = N-1
        
        while digits[last] == 9 and last>=0:
            last = last-1
                    
                
        if last == -1:
            digits = [0] + digits
            last = last+1
            N = N+1
            
        for j in range(last+1,N):
            digits[j] = 0
            
        digits[last] += 1
        
        return digits
        
        
 