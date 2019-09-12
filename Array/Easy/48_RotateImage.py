# 逐个旋转，由外到内每一圈以第一行第一个元素开始旋转四个数
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            point = n - 2 * i + i - 1
            for j in range(i,point):

                temp = matrix[i][j]
                matrix[i][j] = matrix[point-j + i][i]
                matrix[point-j + i][i] = matrix[point][point-j + i]
                matrix[point][point-j + i] = matrix[j][point]
                matrix[j][point] = temp

# 有更快的折叠方法