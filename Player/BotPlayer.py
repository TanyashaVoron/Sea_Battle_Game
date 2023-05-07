import random

from Player.Player import Player


class Bot(Player):
    def __init__(self, field_size, placement_ships):
        super().__init__(field_size, placement_ships)
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.last_move_x, self.last_move_y = 0, 0

    def set_last_move_xy(self, x, y):
        self.last_move_x, self.last_move_y = x, y

    def bot_generation_move(self):
        return str(random.randint(1, self.field_size)) + self.arr_y[random.randint(0, self.field_size - 1)]

    def bot_generation_rational_move(self):
        ships_around = []

        def __deck_check__(_x, _y):
            if self.field_size >= _x > 0 and self.field_size >= _y > 0 and self.field_pattern.get_cell(_x, _y) == '0':
                ships_around.append([_x, _y])

        __deck_check__(self.last_move_x + 1, self.last_move_y)
        __deck_check__(self.last_move_x - 1, self.last_move_y)
        __deck_check__(self.last_move_x, self.last_move_y + 1)
        __deck_check__(self.last_move_x, self.last_move_y - 1)
        __deck_check__(self.last_move_x + 1, self.last_move_y + 1)
        __deck_check__(self.last_move_x + 1, self.last_move_y - 1)
        __deck_check__(self.last_move_x - 1, self.last_move_y + 1)
        __deck_check__(self.last_move_x - 1, self.last_move_y - 1)

        if not ships_around:
            return self.bot_generation_move()
        return ships_around[0]
