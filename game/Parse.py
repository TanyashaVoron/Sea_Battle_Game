class Parse:
    def __init__(self):
        self.arr_x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def parse(self, str):
        if len(str) > 3 and ' ' in str:
            x, y = map(int, str.split())
            if x in self.arr_x and y in self.arr_y:
                return [self.arr_x.index(x) + 1, self.arr_y.index(y) + 1]
        return [0, 0]
