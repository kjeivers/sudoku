from typing import List

from board import *


class Solver:
    def __init__(self, board_str:str):
        self.board = SudokuBoard(board_str)

    def solve(self) -> SudokuBoard:
        return solve_recursively(self.board)

def solve_for_single_missing(board:SudokuBoard):
    for idx, row in enumerate(board.get_rows()):
        number_of_unknowns = len([cell for cell in row if cell.is_value_unknown()])
        if number_of_unknowns > 1:
            print(f"row {idx+1} has {number_of_unknowns} unknowns")
        if number_of_unknowns == 1:
            missing_values = get_missing_values(row)
            get_cell_with_value(row, 0).update_value(missing_values[0])
    for idx, column in enumerate(board.get_columns()):
        number_of_unknowns = len([cell for cell in column if cell.is_value_unknown()])
        if number_of_unknowns > 1:
            print(f"column {idx+1} has {number_of_unknowns} unknowns")
        if number_of_unknowns == 1:
            missing_values = get_missing_values(column)
            get_cell_with_value(column, 0).update_value(missing_values[0])
    for idx, box in enumerate(board.get_boxes()):
        number_of_unknowns = len([cell for cell in box if cell.is_value_unknown()])
        if number_of_unknowns > 1:
            print(f"box {idx+1} has {number_of_unknowns} unknowns")
        if number_of_unknowns == 1:
            missing_values = get_missing_values(box)
            get_cell_with_value(box, 0).update_value(missing_values[0])

# def solve_possible_values(board:SudokuBoard):
#     for cell in board.cells:
#         if cell.is_value_unknown():
#             board.get_row(cell.row_idx)
#             possible_values = get_possible_values(board, cell)
#             if len(possible_values) == 1:
#                 cell.update_value(possible_values[0])

def solve_recursively(start: SudokuBoard) -> SudokuBoard:
    copy = copy_board(start)
    solve_for_single_missing(copy)
    if copy.to_raw_string() == start.to_raw_string():
        return start
    return solve_recursively(copy)
