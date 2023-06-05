class playingField:
    def __init__(self, n):
        self.n = int(n) + 1
        self.field = [['0'] * self.n for _ in range(self.n)]
        self.field[0] = [chr(i) for i in range(64, 65 + self.n)]
        for i in range(self.n):
            self.field[i][0] = i
        self.field[0][0] = '*'

    def get_cell(self, i, j):
        return self.field[i][j]

    def set_cell(self, i, j, val):
        self.field[i][j] = val

    def convert_to_str(self):
        """
        преобразование поля в одну строку (не смайлы)
        """
        field_str = ''
        for i in range(self.n):
            for j in range(self.n):
                field_str += f'{self.field[i][j]} '
        return field_str[:-1]

    def restoration(self, field_str):
        """
        восстановление поля по строке
        """
        field_arr = field_str.split(' ')
        end = field_arr.pop()
        field_arr.append(end.split('\n').pop(0))
        field_arr.reverse()
        for i in range(self.n):
            for j in range(self.n):
                self.field[i][j] = field_arr.pop()
