class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ilist = []
        jlist = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ilist.append(i)
                    jlist.append(j)
 
 
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in ilist or j in jlist:
                    matrix[i][j] = 0
            