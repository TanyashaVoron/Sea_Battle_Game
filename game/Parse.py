class Parse:
    def __init__(self):
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def parse(self, s, n):
        x = y = 0

        if len(s) == 2:
            x = s[0]
            y = s[1]

        if len(s) == 3 and s[0] == '1':
            x = s[0:2]
            y = s[2]

        if 0 < int(x) <= n and y in self.arr_y and self.arr_y.index(y) + 1 <= n:
            return int(x), self.arr_y.index(y) + 1

        return 0, 0
