import random
from Player.Player import Player


class Bot(Player):
    """
    генерация ходов игрока/бота
    """

    def __init__(self, field_size, placement_ships):
        super().__init__(field_size, placement_ships)
        self.arr_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.last_move_x, self.last_move_y = 0, 0

    def bot_generation_move(self):
        """
        рандомная генерация
        """
        return str(random.randint(1, self.field_size)) + self.arr_y[random.randint(0, self.field_size - 1)]

    def bot_generation_rational_move(self):
        """
        умная генерация

        запоминаем последний ход
        смотрим, есть ли вокруг корабли
        если есть, то делаем ход туда
        """
        ships_around = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                _x, _y = self.last_move_x + i, self.last_move_y + j
                if self.field_size >= _x > 0 and self.field_size >= _y > 0 and self.field_pattern.get_cell(_x,
                                                                                                           _y) == '3':
                    ships_around.append([_x, _y])

        for ship in ships_around:
            if self.field_attack.field[ship[0]][ship[1]] == '0':
                return f'{ship[0]}{self.arr_y[ship[1] - 1]}'

        return self.bot_generation_move()
