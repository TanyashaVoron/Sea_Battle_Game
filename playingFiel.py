class playingField:
    def __init__(self, n=10):
        self.n = n + 1
        self.field = [["0"] * self.n for i in range(self.n)]
        self.field[0] = [chr(i) for i in range(64, 65 + self.n)]
        for i in range(self.n):
            self.field[i][0] = i

    def __str__(self):
        result_str = ""
        for i in range(self.n):
            temp_str = ""
            for j in range(self.n):
                temp_str += str(self.field[i][j]) + "  "
            result_str += temp_str + "\n"
        return result_str

    def get_cell(self, i, j):
        return self.field[i][j]

    def set_cell(self, i, j, val):
        self.field[i][j] = val

    # def is_free(self, i, j):
    #     return self.field[i][j] == state_cell.free
    # state_cell(1).name == 'free'


if __name__ == '__main__':
    pass
