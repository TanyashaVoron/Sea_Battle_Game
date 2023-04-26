import random


class Bot:
    def __init__(self):
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def bot_generation_move(self, n):
        return str(random.randint(1, n)) + self.arr_y[random.randint(0, n - 1)]
