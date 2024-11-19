from typing import List

from board import SudokuBoard


class Solver:
    def __init__(self, board_str:str):
        self.board = SudokuBoard(board_str)

    def solve(self) -> SudokuBoard:
        return solve_recursively(self.board)

def solve_for_single_missing(board:SudokuBoard):
    for idx, row in enumerate(board.get_rows()):
        if row.count('-') == 1:
            for i in range(1, 10):
                if str(i) not in row:
                    board.update_cell(idx+1, row.index('-')+1, i)
                    break
    for idx, column in enumerate(board.get_columns()):
        if column.count('-') == 1:
            for i in range(1, 10):
                if str(i) not in column:
                    board.update_cell(column.index('-')+1, idx+1, i)
                    break
    for idx, box in enumerate(board.get_boxes()):
        if box.count('-') == 1:
            for i in range(1, 10):
                if str(i) not in box:
                    board.update_cell(box.index('-')+1, idx+1, i)

def solve_recursively(start: SudokuBoard) -> SudokuBoard:
    copy = SudokuBoard(start.board)
    solve_for_single_missing(copy)
    if copy.board == start.board:
        return start
    return solve_recursively(copy)
