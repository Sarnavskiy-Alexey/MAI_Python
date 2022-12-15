"""
This task was changed from: https://www.codewars.com//kata/56ad7a4978b5162445000056
to: https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    def check_square(self, board, sq_number):
        start = ((sq_number // 3) * 3, (sq_number % 3) * 3)
        line = []
        for i in range(start[0], start[0] + 3):
            for j in range(start[1], start[1] + 3):
                line += [board[i][j]]
        return self.check_line(line)


    def check_line(self, line):
        s = set()
        for el in line:
            if el != '.' and el not in s:
                s.add(el)
            elif el in s:
                return False
        return True


    def transpose_board(self, board):
        for i in range(9):
            for j in range(i):
                board[i][j], board[j][i] = board[j][i], board[i][j]


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check all rows on equal numbers
        for line in board:
            if not self.check_line(line):
                return False
        # check all squares on equal numbers
        for i in range(9):
            if not self.check_square(board, i):
                return False
        # transpose board to apply check_line method again
        self.transpose_board(board)
        # check all columns on equal numbers
        for line in board:
            if not self.check_line(line):
                return False
        return True
