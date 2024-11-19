from typing import List

class SudokuBoard:
    def __init__(self, board:str):
        self.board = board

    # 1-indeksert
    def get_row(self, row:int) -> str:
        return self.board[(row-1)*9:row*9]

    def get_rows(self) -> List[str]:
        return [self.get_row(i) for i in range(1, 10)]

    # 1-indeksert
    def get_column(self, col:int) -> str:
        return ''.join([self.board[(col-1) + 9*i] for i in range(9)])

    def get_columns(self) -> List[str]:
        return [self.get_column(i) for i in range(1, 10)]

    # 1-indeksert
    def get_box(self, box:int) -> str:
        return ''.join([self.board[self.box_position_to_board_index(box, i)] for i in range(1, 10)])

    # 1-indeksert -> column, row
    @staticmethod
    def box_position_to_cell(box:int, number:int) -> (int, int):
        column_offset = ((box-1) % 3) * 3
        row_offset = ((box-1) // 3) * 3
        column = (column_offset + (number-1) % 3) + 1
        row = (row_offset + (number-1) // 3) +1
        return column, row

    # 0-indeksert -> board index
    def box_position_to_board_index(self, box:int, number:int) -> int:
        column, row = self.box_position_to_cell(box, number)
        return (row-1)*9 + column - 1

    def get_boxes(self) -> List[str]:
        return [self.get_box(i) for i in range(1, 10)]

    # 1-indeksert
    def update_cell(self, row:int, col:int, value:int):
        self.board = self.board[:((row-1)*9)+(col-1)] + str(value) + self.board[(row-1)*9+col:]

    def pretty_print(self) -> str:
        return "\n".join([
            self.pretty_print_row(1),
            self.pretty_print_row(2),
            self.pretty_print_row(3),
            "---+---+---",
            self.pretty_print_row(4),
            self.pretty_print_row(5),
            self.pretty_print_row(6),
            "---+---+---",
            self.pretty_print_row(7),
            self.pretty_print_row(8),
            self.pretty_print_row(9),
        ])

    def pretty_print_row(self, row:int) -> str:
        row = self.get_row(row)
        return f"{row[:3]}|{row[3:6]}|{row[6:]}"

    def solve_for_single_missing(self):
        for idx, row in enumerate(self.get_rows()):
            if row.count('-') == 1:
                for i in range(1, 10):
                    if str(i) not in row:
                        self.update_cell(idx+1, row.index('-')+1, i)
                        break
        for idx, column in enumerate(self.get_columns()):
            if column.count('-') == 1:
                for i in range(1, 10):
                    if str(i) not in column:
                        self.update_cell(column.index('-')+1, idx+1, i)
                        break
        for idx, box in enumerate(self.get_boxes()):
            if box.count('-') == 1:
                for i in range(1, 10):
                    if str(i) not in box:
                        self.update_cell(box.index('-')+1, idx+1, i)
                        break

def solve(board_str:str) -> SudokuBoard:
    board = SudokuBoard(board_str)
    return solve_recursively(board)

def solve_recursively(start: SudokuBoard) -> SudokuBoard:
    copy = SudokuBoard(start.board)
    copy.solve_for_single_missing()
    if copy.board == start.board:
        return start
    return solve_recursively(copy)
