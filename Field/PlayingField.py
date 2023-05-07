class playingField:
    def __init__(self, n):
        self.n = int(n) + 1
        self.field = [['0'] * self.n for _ in range(self.n)]
        self.field[0] = [chr(i) for i in range(64, 65 + self.n)]
        for i in range(self.n):
            self.field[i][0] = i
        self.field[0][0] = ' '

    def get_cell(self, i, j):
        return self.field[i][j]

    def set_cell(self, i, j, val):
        self.field[i][j] = val


if __name__ == '__main__':
    pass
