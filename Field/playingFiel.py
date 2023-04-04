class playingField:
    def __init__(self, n=10):
        self.n = n + 1
        self.field = [['0'] * self.n for _ in range(self.n)]
        self.field[0] = [chr(i) for i in range(64, 65 + self.n)]
        for i in range(self.n):
            self.field[i][0] = i
        self.field[0][0] = ' '

    def field_in_string(self):
        map_transform_desk = {'0': '◼️', '1': '🚢', '2': '🗯', '3': '🚢', '?': '❔', '!':'❗️'}
        result_str = ' '
        for i in range(self.n):
            temp_str = ''
            for j in range(self.n):
                if j != 0 and i != 0:
                    temp_str += str(map_transform_desk.get(self.field[i][j])) + ' '
                    # temp_str += str(self.field[i][j]) + "  "
                elif i == 10:
                    temp_str += str(self.field[i][j])+' '
                else:
                    temp_str += str(self.field[i][j]) + '  '
            result_str += temp_str + "\n"
        return result_str

    def get_cell(self, i, j):
        return self.field[i][j]

    def set_cell(self, i, j, val):
        self.field[i][j] = val


if __name__ == '__main__':
    pass
