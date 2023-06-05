import os

from Player.BotPlayer import Bot


class Save:
    """
    сохранение и восстановление игры
    """

    def __init__(self):
        self.filepath = os.path.join(
            os.path.expanduser('/Users/tatanavoronina/PycharmProjects/Sea-Battle-Game/uplouds'),
            'Sea_battle_game_info.txt')  # такой путь сделан для теста
        self.is_saved_game = False

    def is_saved(self):
        """
        проверка на существование сохраненной игры
        """
        self.is_saved_game = os.path.isfile(self.filepath)

    def to_restore(self):
        """
        изьятие компонентов игры из файла
        """
        with open(self.filepath, 'r') as f:
            field_size = int(f.readline())
            ships = int(f.readline())
            player_1 = Bot(field_size, ships)
            player_2 = Bot(field_size, ships)
            is_move = int(f.readline())
            player_1.count_cell = int(f.readline())
            player_2.count_cell = int(f.readline())
            player_1.field_attack.restoration(f.readline())
            player_2.field_attack.restoration(f.readline())
            player_1.field_pattern.restoration(f.readline())
            player_2.field_pattern.restoration(f.readline())
            count_players = int(f.readline())
            difficultly = int(f.readline())
            return player_1, player_2, is_move, ships, field_size, count_players, difficultly

    def to_save(self, player_1, player_2, is_move, ships, field_size, count_players, difficultly):
        """
        сохранение компонентов игры в файл
        """
        with open(self.filepath, 'w') as f:
            f.write(f'{field_size}\n')
            f.write(f'{ships}\n')
            f.write(f'{is_move}\n')
            f.write(f'{player_1.count_cell}\n')
            f.write(f'{player_2.count_cell}\n')
            f.write(f'{player_1.field_attack.convert_to_str()}\n')
            f.write(f'{player_2.field_attack.convert_to_str()}\n')
            f.write(f'{player_1.field_pattern.convert_to_str()}\n')
            f.write(f'{player_2.field_pattern.convert_to_str()}\n')
            f.write(f'{count_players}\n')
            f.write(f'{difficultly}\n')
