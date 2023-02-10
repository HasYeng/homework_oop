import Spreadsheet
import Cell


def test_set_get_cell_at(sp: Spreadsheet.Spreadsheet, row, column, val):
    try:
        sp.set_cell_at(row, column, val)

        if isinstance(val, Spreadsheet.Cell.Cell):
            if sp.get_cell_at(row, column).get_value() == val.get_value() and \
                    sp.get_cell_at(row, column).get_color() == val.get_color():
                print("test_set_get_cell_at succeeded")
            else:
                print("test_set_get_cell_at failed")
        else:
            if sp.get_cell_at(row, column).get_value() != str(val):
                print("test_set_get_cell_at failed")
            else:
                print("test_set_get_cell_at succeeded")
    except ValueError:
        print("test_set_get_cell_at succeeded")


def test_add_row(sp: Spreadsheet.Spreadsheet, row):
    try:
        if row == sp.row-1:
            sp.add_row(row)
            try:
                sp.set_cell_at(row+1, 1, "hello")
                print("test_add_row succeeded")
            except:
                print("test_add_row failed")
        else:
            sp.set_cell_at(row + 1, 1, "hello")
            sp.add_row(row)
            if sp.get_cell_at(row + 2, 1).get_value() == "hello":
                print("test_add_row succeeded")
            else:
                print("test_add_row failed")
    except ValueError:
        print("test_add_row succeeded")


def test_remove_row(sp: Spreadsheet.Spreadsheet, row):
    try:
        if row == sp.row-1:
            sp.remove_row(row)
            try:
                sp.set_cell_at(row+1, 1, "hello")
                print("test_remove_row failed")
            except:
                print("test_remove_row succeeded")
        else:
            sp.set_cell_at(row + 1, 1, "hello")
            sp.remove_row(row)
            if sp.get_cell_at(row, 1).get_value() == "hello":
                print("test_remove_row succeeded")
            else:
                print("test_remove_row failed")
    except ValueError:
        print("test_remove_row succeeded")


def test_add_column(sp: Spreadsheet.Spreadsheet, column):
    try:
        if column == sp.column-1:
            sp.add_column(column)
            try:
                sp.set_cell_at(1, column+1, "hello")
                print("test_add_column succeeded")
            except:
                print("test_add_column failed")
        else:
            sp.set_cell_at(1, column+1, "hello")
            sp.add_column(column)
            if sp.get_cell_at(1, column+2).get_value() == "hello":
                print("test_add_column succeeded")
            else:
                print("test_add_column failed")
    except ValueError:
        print("test_add_column succeeded")


def test_remove_column(sp: Spreadsheet.Spreadsheet, column):
    try:
        if column == sp.column-1:
            sp.remove_column(column)
            try:
                sp.set_cell_at(1, column+1, "hello")
                print("test_remove_column failed")
            except:
                print("test_remove_column succeeded")
        else:
            sp.set_cell_at(1, column+1, "hello")
            sp.remove_column(column)
            if sp.get_cell_at(1, column).get_value() == "hello":
                print("test_remove_column succeeded")
            else:
                print("test_remove_column failed")
    except ValueError:
        print("test_remove_column succeeded")


def test_swap_rows(sp: Spreadsheet.Spreadsheet, row1, row2):
    try:
        sp.set_cell_at(row1, 1, "hello1")
        sp.set_cell_at(row2, 1, "hello2")
        sp.swap_rows(row1, row2)
        if sp.get_cell_at(row1, 1).get_value() == "hello2" and \
                sp.get_cell_at(row2, 1).get_value() == "hello1":
            print("test_swap_rows succeeded")
        else:
            print("test_swap_rows failed")
    except ValueError:
        print("test_swap_rows succeeded")


def test_swap_columns(sp: Spreadsheet.Spreadsheet, columns1, columns2):
    try:
        sp.set_cell_at(1, columns1, "hello1")
        sp.set_cell_at(1, columns2, "hello2")
        sp.swap_columns(columns1, columns2)
        if sp.get_cell_at(1, columns1).get_value() == "hello2" and \
                sp.get_cell_at(1, columns2).get_value() == "hello1":
            print("test_swap_columns succeeded")
        else:
            print("test_swap_columns failed")
    except ValueError:
        print("test_swap_columns succeeded")

def test(sp):
    test_set_get_cell_at(sp, 3, 4, "hello")
    test_set_get_cell_at(sp, 2, 3, 77)
    test_set_get_cell_at(sp, 2, 3, Cell.Cell("hello", 3))
    test_set_get_cell_at(sp, 2, 83, Cell.Cell("hello", 3))
    test_add_row(sp, 4)
    test_add_row(sp, 0)
    test_add_row(sp, 8)
    test_remove_row(sp, 6)
    test_remove_row(sp, 0)
    test_remove_row(sp, 9)
    test_add_column(sp, 4)
    test_add_column(sp, 0)
    test_add_column(sp, 8)
    test_remove_column(sp, 4)
    test_remove_column(sp, 0)
    test_remove_column(sp, 9)
    test_swap_rows(sp, 0, 4)
    test_swap_rows(sp, 8, 56)
    test_swap_columns(sp, 0, 4)
    test_swap_columns(sp, 0, 77)


s = Spreadsheet.Spreadsheet(4, 5)
test(s)