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

                            "5C", "6G",
                            "3D",
                            "3A",
                            "6A"
                            ]

        return array_of_inputs1[i]
