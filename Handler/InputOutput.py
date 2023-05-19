class Input_Output:

    def output_win(self, player):
        return 'победил игрок' + str(player)

    def output_fields(self, field_pattern, field_attack, n, turn):
        field = f'ход игрока номер {turn}\n'
        field += '             игрок 1                                          игрок 2\n'
        field_pattern = self.to_string_field(field_pattern, n).split('\n')
        field_attack = self.to_string_field(field_attack, n).split('\n')

        for i in range(len(field_pattern) - 1):
            field += ' ' + field_pattern[i] + '   ' + field_attack[i] + '\n'

        return field

    def output_field(self, field, n, num):
        return f'pасстановка {num} игррока\n' + self.to_string_field(field, n)

    def to_string_field(self, field, n):
        n += 1
        map_transform_desk = {'0': '◼️', '1': '🚢', '2': '🗯', '3': '🚢', '?': '❔', '!': '❗️', '+': '+'}
        result_str = ' '
        for i in range(n):
            temp_str = ''
            if i == 0:
                temp_str += ' '
            if i < 10:
                temp_str += '  '
            for j in range(n):
                if i==0 and (j==9 or j==10):
                    temp_str += ' '
                if j != 0 and i != 0:
                    temp_str += str(map_transform_desk.get(field[i][j])) + ' '
                elif i == n:
                    temp_str += str(field[i][j]) + ' '
                else:
                    temp_str += str(field[i][j]) + '  '
            result_str += temp_str + "\n"
        return result_str
