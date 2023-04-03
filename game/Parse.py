class Parse:
    def __init__(self):
        self.arr_x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def parse(self, s):
        x = y = 0

        if len(s) == 2:
            x = s[0]
            y = s[1]

        if len(s) == 3 and s[0] == '1':
            x = s[0:2]
            y = s[2]

        if x in self.arr_x and y in self.arr_y:
            return self.arr_x.index(x) + 1, self.arr_y.index(y) + 1

        return 0, 0
