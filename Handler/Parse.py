class Parse:
    def __init__(self):
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def parse(self, turn, field_size):
        """
        парсинг хода игрока
        """
        x = y = 0
        if len(turn) == 1 or len(turn) > 3:
            return 0, 0

        if len(turn) == 2:
            x = turn[0]
            y = turn[1]

        if len(turn) == 3 and turn[0] == '1':
            x = turn[0:2]
            y = turn[2]

        if str(x).isdigit() and x not in self.arr_y and 0 < int(
                x) <= field_size and y in self.arr_y and self.arr_y.index(
                y) + 1 <= field_size:
            return int(x), self.arr_y.index(y) + 1

        return 0, 0
