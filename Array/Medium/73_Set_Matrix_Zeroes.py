# 在使用常数额外空间下，可以使用每一行的第一位代表改行是否为0，每一列的第一位代表该列是否为0，但是要注意，第一行第一列就会有两个代表含义，会造成困惑，所以要额外添加变量用于解决该位置的信息表示
# 最快解法使用n+m空间复杂度，记录哪一行哪一列需要修改为0
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return
        elif not matrix[0]:
            return
        n = len(matrix)
        m = len(matrix[0])
        
        first_row = False
        first_column = False
        
        for i in range(n):
            
            for j in range(m):
                
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_column = True
        
        for j in range(1,m):
            
            if matrix[0][j] == 0:
                
                for i in range(1,n):
                    matrix[i][j] = 0
        
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(1,m):
                    matrix[i][j] = 0
        
        if first_row:
            for j in range(m):
                matrix[0][j] = 0
        if first_column:
            for i in range(n):
                matrix[i][0] = 0
            
            