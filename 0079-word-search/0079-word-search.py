class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True

        return False

    def dfs(self, board, i, j, word):
        if word == '':
            return True
        
        if 0<=i<len(board) and 0<=j<len(board[0]):
            temp = board[i][j]
            if temp == word[0]:
                board[i][j] = '#'
                word = word[1:]
                if self.dfs(board, i + 1, j , word) or self.dfs(board, i - 1, j , word) or  self.dfs(board, i , j - 1, word) or self.dfs(board, i , j + 1, word):
                    return True
                else:
                    board[i][j] = temp