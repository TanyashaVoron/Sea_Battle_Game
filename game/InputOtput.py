class Input_Otput:

    def input_str(self):
        print('введите координаты: ')
        return input()

    def output_str(self, str):
        print(str)

    def output_exe(self):
        print('ошибка ввода. попробуйте еще раз')

    def output_win(self, player):
        print('подебил игрок' + str(player))

    def output_seating(self, player):
        print(f'расстановка игрока {player}')

    def output_finish_seating(self):
        print('расстановка окончена \nначинаем игру!')

    def output_fields(self, field_pattern, field_attack, is_player):
        field = '                                player' + str(is_player) + '\n'
        field += '           attack field                          my field\n'
        field_pattern = field_pattern.split('\n')
        field_attack = field_attack.split('\n')

        for i in range(len(field_pattern) - 2):
            field += ' ' + field_pattern[i] + '   ' + field_attack[i] + '\n'
        field += field_pattern[-2] + '  ' + field_attack[-2] + '\n'

        print(field)

    def input_from_array(self, i):
        array_of_inputs1 = ['5A', '4A',
                            '8C', '8D',
                            '1H', '1I',
                            "4G", "6G",
                            "7I", "7J",
                            "9H", "10H",
                            "3D", "8A",
                            "5E", "10D",
                            "5A", "4A",
                            "8C", "8D",
                            "1H", "1I",
                            "4G", "6G",
                            "7I", "7J",
                            "9H", "10H",
                            "3D", "8A",
                            "5E", "10D",
                            ]

        return array_of_inputs1[i]
