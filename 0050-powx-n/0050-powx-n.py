class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        
        N = abs(n)
        
        rem = N
        total = 1
        while rem > 0:
            y, power = self.quad(x,rem)
            rem = rem - power
            total = total * y
            
        if n<0:
            total = 1/total
            
        return total
    
    def quad(self, x, N):
        y = x
        power = 1
        while power*2 < N:
            y = y*y
            power = power*2
        return y, power