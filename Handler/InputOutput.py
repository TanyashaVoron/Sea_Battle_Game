class Input_Output:
    def input(self):
        return input()

    def output_start(self):
        print('Привет! пиши start, как решишь поиграть')

    def questions_quick_start(self):
        print('Настройки по умолчанию или новые? да/нет')
        print('''настройки по умолчанию:
        размер поля 10х10
        прямые корабли
        игра с ботом
        легкий уровень сложности
        автоматическая расстановка кораблей
        игра без времени''')

    def questions_size_field(self):
        print('Выбери размер поля, напиши число 10, 15 или 20')

    def questions_ships(self):
        print('Круто! Теперь корабли! Ты хочешь стандартные прямые(straight) или необычные угловые(angular) корабли?')

    def questions_count_players(self):
        print('Ты хочешь играть со мной(bot) или с другом(friend)?')

    def questions_difficultly(self):
        print('Воу, класс! Хм, но я могу играть как профи ли как новичек, давай ты выберешь уровень: простой(easy) или '
              'сложныйт(hard)')

    def questions_filling(self):
        print('Ох, еще немного. Кто расставит корабли: автоматически(machine) или сам(hands)')

    def questions_time(self):
        print('Иии, последний вопрос. Поиграем на время ( у тебя будет 5 минут ) ? да/нет')

    def input_coordinates(self):
        print('введите координаты (без пробелов цифра, буква): ')
        return self.input()

    def output_str(self, str):
        print(str)

    def output_exe(self):
        print('ошибка ввода. попробуйте еще раз')

    def output_win(self, player):
        print('победил игрок' + str(player))

    def output_seating(self, player):
        print(f'расстановка игрока {player}')

    def output_finish_seating(self):
        print('расстановка окончена \nначинаем игру!')

    def output_fields(self, field_pattern, field_attack, n):
        #field = '                                player' + str(is_player) + '\n'
        field = '           player 1                             player 2\n'
        field_pattern = self.to_string_field(field_pattern, n).split('\n')
        field_attack = self.to_string_field(field_attack, n).split('\n')

        for i in range(len(field_pattern) - 1):
            field += ' ' + field_pattern[i] + '   ' + field_attack[i] + '\n'


        print(field)

    def output_field(self, field, n):
        print(self.to_string_field(field, n))

    def to_string_field(self, field, n):
        n+=1
        map_transform_desk = {'0': '◼️', '1': '🚢', '2': '🗯', '3': '🚢', '?': '❔', '!': '❗️', '+': '+'}
        result_str = ' '
        for i in range(n):
            temp_str = ''
            if i <10:
                temp_str+=' '
            for j in range(n):
                if j != 0 and i != 0:
                    temp_str += str(map_transform_desk.get(field[i][j])) + ' '
                elif i == n:
                    temp_str += str(field[i][j]) + ' '
                else:
                    temp_str += str(field[i][j]) + '  '
            result_str += temp_str + "\n"
        return result_str
