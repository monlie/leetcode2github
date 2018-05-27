class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.mat = [[0] * n for _ in range(m)]
        self.mat[0][0] = matrix[0][0]
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                if not i:
                    self.mat[i][j] = self.mat[i][j-1] + matrix[i][j]
                elif not j:
                    self.mat[i][j] = self.mat[i-1][j] + matrix[i][j]
                else:
                    self.mat[i][j] = self.mat[i-1][j] + self.mat[i][j-1] - self.mat[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not row1 and not col1:
            return self.mat[row2][col2]
        elif not row1:
            return self.mat[row2][col2] - self.mat[row2][col1-1]
        elif not col1:
            return self.mat[row2][col2] - self.mat[row1-1][col2]
        return self.mat[row2][col2] - self.mat[row2][col1-1] - self.mat[row1-1][col2] + self.mat[row1-1][col1-1]
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
