from typing import List

from board import *


class Solver:
    def __init__(self, board: Union[str,SudokuBoard]):
        if isinstance(board, str):
            self.board = SudokuBoard(board)
        else:
            self.board = board

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

def solve_possible_values(board:SudokuBoard):
    def remove_from_possible_values(cell:Cell, lst:List[Cell]):
        for item in lst:
            if not item.is_value_unknown():
                cell.remove_from_possible_values(item.value)

    for cell in board.cells:
        if cell.is_value_unknown():
            # check rows, columns and boxes for already used values
            remove_from_possible_values(cell, board.get_row(cell.row_idx))
            remove_from_possible_values(cell, board.get_column(cell.col_idx))
            remove_from_possible_values(cell,  board.get_box(cell.box_idx))

            if len(cell.possible_values) == 1:
                cell.update_value(next(iter(cell.possible_values)))

    def is_only_possible_in_this_cell(cell:Cell, value:int, lst:List[Cell]) -> bool:
        for other_cell in lst:
            if other_cell != cell and value in other_cell.possible_values:
                return False
        return True

    for cell in board.cells:
        if cell.is_value_unknown():
            for value in cell.possible_values:
                # check if value is only possible in row, column or box
                if is_only_possible_in_this_cell(cell, value, board.get_row(cell.row_idx)):
                    cell.update_value(value)
                    break
                if is_only_possible_in_this_cell(cell, value, board.get_column(cell.col_idx)):
                    cell.update_value(value)
                    break
                if is_only_possible_in_this_cell(cell, value, board.get_box(cell.box_idx)):
                    cell.update_value(value)
                    break

def solve_recursively(start: SudokuBoard) -> SudokuBoard:
    copy = copy_board(start)
    # solve_for_single_missing(copy)
    solve_possible_values(copy)
    if copy.to_raw_string() == start.to_raw_string():
        return start
    return solve_recursively(copy)
