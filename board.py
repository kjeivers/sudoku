from typing import List, Union


class Cell:
    def __init__(self, row_idx:int, col_idx:int, value:int):
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.box_idx = (col_idx // 3) + 3 * (row_idx // 3)
        self.value = value
        self.possible_values = set(range(1, 10)) if value == 0 else {value}

    def __str__(self) -> str:
        return '-' if self.value == 0 else str(self.value)

    def update_value(self, value):
        self.value = value
        if value != 0:
            self.possible_values = {value}

    def is_value_unknown(self) -> bool:
        return self.value == 0


class SudokuBoard:
    def __init__(self, board: Union[str, List[Cell]]):
        self.cells = []
        self.rows = [list() for _ in range(0, 9)]
        self.columns = [list() for _ in range(0, 9)]
        self.boxes = [list() for _ in range(0, 9)]
        if isinstance(board, str):
            self.from_raw_string(board)
        else:
            self.from_cells(board)

    def from_raw_string(self, raw_board):
        self.cells = []
        for index, char in enumerate(raw_board):
            row_idx = index // 9
            col_idx = index % 9
            cell = Cell(row_idx, col_idx, 0 if char == '-' else int(char))
            self.cells.append(cell)
            self.rows[row_idx].append(cell)
            self.columns[col_idx].append(cell)
            self.boxes[cell.box_idx].append(cell)

    def from_cells(self, cells: List[Cell]):
        self.cells = cells
        for cell in cells:
            self.rows[cell.row_idx].append(cell)
            self.columns[cell.col_idx].append(cell)
            self.boxes[cell.box_idx].append(cell)

    def to_raw_string(self) -> str:
        return "".join([str(cell) for cell in self.cells])

    def pretty_print(self) -> str:
        return "\n".join([
            self.pretty_print_row(0),
            self.pretty_print_row(1),
            self.pretty_print_row(2),
            "---+---+---",
            self.pretty_print_row(3),
            self.pretty_print_row(4),
            self.pretty_print_row(5),
            "---+---+---",
            self.pretty_print_row(6),
            self.pretty_print_row(7),
            self.pretty_print_row(8),
        ])

    def pretty_print_row(self, row_idx:int) -> str:
        row_cells = self.rows[row_idx]
        return f"{row_cells[0]}{row_cells[1]}{row_cells[2]}|{row_cells[3]}{row_cells[4]}{row_cells[5]}|{row_cells[6]}{row_cells[7]}{row_cells[8]}"

    def get_row(self, row_idx:int) -> List[Cell]:
        return self.rows[row_idx]

    def get_column(self, column_idx:int) -> List[Cell]:
        return self.columns[column_idx]

    def get_box(self, box_idx:int) -> List[Cell]:
        return self.boxes[box_idx]

    def get_row_str(self, row_idx:int) -> str:
        return "".join([str(cell) for cell in self.get_row(row_idx)])

    def get_column_str(self, column_idx:int) -> str:
        return "".join([str(cell) for cell in self.get_column(column_idx)])

    def get_box_str(self, box_idx:int) -> str:
        return "".join([str(cell) for cell in self.get_box(box_idx)])

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_boxes(self):
        return self.boxes

    def update_cell(self, column_idx: int, row_idx: int, value: int):
        self.get_cell(column_idx, row_idx).update_value(value)

    def get_cell(self, column_idx, row_idx) -> Cell:
        return self.get_column(column_idx)[row_idx]


def copy_board(board:SudokuBoard) -> SudokuBoard:
    return SudokuBoard([Cell(cell.row_idx, cell.col_idx, cell.value) for cell in board.cells])

def get_cell_with_value(lst: List[Cell], value: int) -> Union[Cell, None]:
    for cell in lst:
        if cell.value == value:
            return cell
    return None

def get_missing_values(lst: List[Cell]) -> List[int]:
    missing_values = []
    for i in range(1, 10):
        if get_cell_with_value(lst, i) is None:
            missing_values.append(i)
    return missing_values