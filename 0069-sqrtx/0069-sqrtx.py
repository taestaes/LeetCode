class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        for y in range(2**16):
            if y*y == x:
                return y
            elif y*y > x:
                return y-1