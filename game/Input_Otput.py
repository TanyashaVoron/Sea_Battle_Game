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
