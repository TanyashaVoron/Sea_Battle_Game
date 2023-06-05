class Output:
    """
    класса для вывода текстовой информации в gui
    """

    def __init__(self):
        '''
        подгонка строки под размер поля
        по другому нельзя из-за разницы в шрифтах и ширине букв
        разное кол-во пробелов - так и должно быть
        '''
        self.ABC = {
            10: '      A  B  C  D  E  F  G  H   I   J  \n',
            15: '      A  B  C  D   E  F  G  H   I   J   K  L  M  N  O  \n',
            20: '      A   B   C    D    E   F   G   H    I    J    K   L    M   N   O   P   Q   R    S   T   \n'}
        self.SPACE = {
            10: ' ' * 40,
            15: ' ' * 67,
            20: ' ' * 113
        }

    def win(self, player):
        return f'победил игрок {str(player)}'

    def draw(self):
        return 'ничья!'

    def error(self):
        return 'ошибка ввода'

    def instructions(self):
        return 'введите координаты\n(без пробелов цифра, буква)\nнажмите кнопку ВВОД'

    def fields(self, field_pattern, field_attack, field_size, turn):
        """
        конвертация двух полей в одну строку
        """
        field = f'ход игрока номер {turn}\n'
        field += f'             игрок 1{self.SPACE[field_size]}игрок 2\n'
        field_pattern = self.to_string_field(field_pattern, field_size).split('\n')
        field_attack = self.to_string_field(field_attack, field_size).split('\n')

        for i in range(len(field_pattern) - 1):
            field += ' ' + field_pattern[i] + '   ' + field_attack[i] + '\n'

        return field

    def field(self, field, n, num):
        return f'pасстановка {num} игрока\n{self.to_string_field(field, n)}'

    def to_string_field(self, field, field_size):
        """
        конвертация поля игрока в строку с смайлами
        """
        field_size += 1
        map_transform_desk = {'0': '◼️', '1': '🚢', '2': '🗯', '3': '🚢', '?': '❔', '!': '❗️', '+': '+'}
        result_str = f' {self.ABC[field_size - 1]}'
        for i in range(1, field_size):
            temp_str = ''
            if i == 0:
                temp_str += ' '
            if i < 10:
                temp_str += '  '
            for j in range(field_size):
                if i == 0 and j == 0:
                    temp_str += ' '
                if i == 0 and (j == 9 or j == 10):
                    temp_str += ' '
                if j != 0 and i != 0:
                    temp_str += str(map_transform_desk.get(field[i][j])) + ' '
                elif i == field_size:
                    temp_str += str(field[i][j]) + ' '
                else:
                    temp_str += str(field[i][j]) + '  '
            result_str += temp_str + "\n"
        return result_str
