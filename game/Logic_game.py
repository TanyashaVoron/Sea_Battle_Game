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
        while self.state != 'finish':
            x, y = self.parse.parse(self.input_output.input_str())

            if x == 0 and y == 0:
                self.input_output.output_exe()
                return

            if self.state == 'start':
                self.state = 'seating'

            if self.state == 'seating':
                while not self.player1.end_of_placement():
                    self.player1.put_ship(x, y)
                    # вывод текущего заполнения
                    print(self.player1.show_field_pattern())

                while not self.player2.end_of_placement():
                    self.player2.put_ship(x, y)

                self.state = 'game'

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
                    else:
                        self.player2.do_step(x, y)


if __name__ == '__main__':
    game = Game()
    game.run()
