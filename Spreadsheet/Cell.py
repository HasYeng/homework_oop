import datetime

colors = {0: "white",
          1: "red",
          2: "black",
          3: "purple",
          4: "yellow"}


class Cell:

    def __init__(self, value="", color=0):
        self._value = value
        self._color = colors[color]

    def set_value(self, string: str):
        self._value = str(string)

    def set_color(self, color: int):
        if color in set(range(5)):
            self._color = colors[color]
        else:
            raise ValueError

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def to_int(self):
        return int(self._value)

    def to_double(self):
        return float(self._value)

    def to_date(self):
        return datetime.date(int(self._value[:4]), int(self._value[5:7]), int(self._value[8:]))

    def reset(self):
        self._color = "white"
        self._value = ""

