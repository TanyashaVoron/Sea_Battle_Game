from Input_Otput import Input_Otput
from Parse import Parse
from game.Player import Player


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.state = 'start'
        self.whose_move_bool = False
        self.input_output = Input_Otput()
        self.parse = Parse()

    def run(self):
        i = 0
        while self.state != 'finish':
            # x, y = self.parse.parse(self.input_output.input_str())
            x, y = self.parse.parse(self.input_output.input_from_array(i))
            i += 1

            if x == 0 and y == 0:
                self.input_output.output_exe()
                return

            if self.state == 'start':
                self.state = 'seating'

            if self.state == 'seating':
                if not self.player1.end_of_placement():
                    self.player1.put_ship(x, y)

                elif not self.player2.end_of_placement():
                    self.player2.put_ship(x, y)

                else:
                    self.state = 'game'
                    print("after placement:")
                    print(self.player1.show_field_pattern())
                    print(self.player1.show_field_pattern())


                # вывод текущего заполнения
                # print(self.player1.show_field_pattern())

            if self.state == 'game':
                if self.player1.count_cell == 0:
                    self.input_output.output_win(1)
                    self.state = 'finish'
                elif self.player2.count_cell == 0:
                    self.input_output.output_win(2)
                    self.state = 'finish'
                else:
                    if self.whose_move_bool:
                        self.player1.do_step(x, y)
                        print("player1")
                        print(self.player1.show_field_pattern())

                    else:
                        self.player2.do_step(x, y)
                        print("player2")
                        print(self.player2.show_field_pattern())


if __name__ == '__main__':
    game = Game()
    game.run()
