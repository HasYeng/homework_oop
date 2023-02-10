import numpy as np
import Cell
import copy


class Spreadsheet:
    def __init__(self, row: int, column: int):
        if isinstance(row, int) and isinstance(column, int) and row > 0 and column > 0:
            self.row = row
            self.column = column
            self.spreadsheet = [[Cell.Cell() for _ in range(column)] for _ in range(row)]
        else:
            raise ValueError

    def set_cell_at(self, row: int, column: int, cell_or_txt: Cell.Cell | str):
        if isinstance(row, int) and isinstance(column, int) and 0 <= row < self.row and 0 <= column < self.column:
            if isinstance(cell_or_txt, Cell.Cell):
                self.spreadsheet[row][column] = copy.deepcopy(cell_or_txt)
            else:
                self.spreadsheet[row][column].set_value(str(cell_or_txt))
        else:
            raise ValueError

    def get_cell_at(self, row: int, column: int):
        if isinstance(row, int) and isinstance(column, int) and 0 <= row < self.row and 0 <= column < self.column:
            return self.spreadsheet[row][column]
        else:
            raise ValueError

    def add_row(self,  row: int):
        if isinstance(row, int) and 0 <= row < self.row:
            self.spreadsheet.insert(row, [Cell.Cell() for _ in range(self.column)])
            self.row += 1
        else:
            raise ValueError

    def remove_row(self, row: int):
        if isinstance(row, int) and 0 <= row < self.row:
            del self.spreadsheet[row]
            self.row -= 1
        else:
            raise ValueError

    def add_column(self, column: int):
        if isinstance(column, int) and 0 <= column < self.row:
            for col in self.spreadsheet:
                col.insert(column, Cell.Cell())
            self.column += 1
        else:
            raise ValueError

    def remove_column(self, column: int):
        if isinstance(column, int) and 0 <= column < self.column:
            for col in self.spreadsheet:
                del col[column]
            self.column -= 1
        else:
            raise ValueError

    def swap_rows(self, row1: int, row2: int):
        if isinstance(row1, int) and 0 <= row1 < self.row and isinstance(row2, int) and 0 <= row2 < self.row:
            self.spreadsheet[row1], self.spreadsheet[row2] = self.spreadsheet[row2], self.spreadsheet[row1]
        else:
            raise ValueError

    def swap_columns(self, column1: int, column2: int):
        if isinstance(column1, int) and 0 <= column1 < self.column and isinstance(column1, int) \
                and 0 <= column2 < self.column:
            self.spreadsheet[column1], self.spreadsheet[column2] = self.spreadsheet[column2], self.spreadsheet[column1]
        else:
            raise ValueError

