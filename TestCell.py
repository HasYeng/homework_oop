# Tests for cell
import Cell
import datetime


def test_set_get_value(cell: Cell.Cell, val):
    cell.set_value(val)
    if cell.get_value() != str(val):
        print("test_set_value failed")
    else:
        print("test_set_value succeeded")


def test_set_get_color(cell: Cell.Cell, color):
    try:
        colors = {0: "white",
                  1: "red",
                  2: "black",
                  3: "purple",
                  4: "yellow"}
        cell.set_color(color)
        if cell.get_color() != colors[color]:
            print("test_set_get_color failed")
        else:
            print("test_set_get_color succeeded")
    except ValueError:
        print("test_set_get_color succeeded")


def test_to_int(cell: Cell.Cell, val):
    cell.set_value(val)
    try:
        if cell.to_int() != int(val):
            print("test_to_int failed")
        else:
            print("test_to_int succeeded")
    except ValueError:
        print("test_to_int succeeded")


def test_to_double(cell: Cell.Cell, val):
    cell.set_value(val)
    try:
        if cell.to_double() != float(val):
            print("test_to_double failed")
        else:
            print("test_to_double succeeded")
    except ValueError:
        print("test_to_double succeeded")


def test_to_date(cell: Cell.Cell, val):
    cell.set_value(val)
    try:
        if cell.to_date() != datetime.date(int(val[:4]), int(val[5:7]), int(val[8:])):
            print("test_to_date failed")
        else:
            print("test_to_date succeeded")
    except ValueError:
        print("test_to_date succeeded")


def test_reset(cell: Cell.Cell, val):
    cell.set_value(val)
    cell.reset()
    if cell.get_value() == "" and cell.get_color() == "white":
        print("test_reset succeeded")
    else:
        print("test_reset failed")


def test(t_cell):
    test_set_get_value(t_cell, "hello")
    test_set_get_value(t_cell, 1)
    test_set_get_color(t_cell, 3)
    test_set_get_color(t_cell, 38)
    test_to_int(t_cell, 1)
    test_to_int(t_cell, -1.8)
    test_to_int(t_cell, "hello")
    test_to_double(t_cell, 1.7)
    test_to_double(t_cell, "hello")
    test_to_date(t_cell, "hello")
    test_to_date(t_cell, "2004-06-08")
    test_reset(t_cell, "hello")


test(Cell.Cell())