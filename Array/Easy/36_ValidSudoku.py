# 扫描数独，用一个9*3*9的数组来记录数字k在j行/列/九宫格出现次数，出现超过1次以上就是不合格

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_list = [[[0 for i in range(9)] for i in range(3)] for i in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                num_list[int(board[i][j]) - 1][0][i] += 1
                num_list[int(board[i][j]) - 1][1][j] += 1
                num_list[int(board[i][j]) - 1][2][i//3*3+j//3] += 1

        for k in range(9):
            for i in range(3):
                for j in range(9):

                    if num_list[k][i][j] > 1:
                        return False

        return True

# 思路类似，使用set()加快了运算
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        big = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i//3,j//3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i//3,j//3,cur))
        return True