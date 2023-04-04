from InputOtput import Input_Otput
from Parse import Parse
from Player import Player
from BotPlayer import Bot


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.state = 'start'
        self.whose_move_bool = 1
        self.input_output = Input_Otput()
        self.parse = Parse()
        self.bot = Bot()

    def run(self, num_of_players, size_field):
        #i = 0
        while self.state != 'finish':
            if self.state == 'start':
                self.state = 'seating'
                self.input_output.output_seating(1)
                print(self.player1.show_field_pattern().field_in_string())

            if num_of_players == 1 and self.whose_move_bool == 1:
                x, y = self.parse.parse(self.bot.bot_generation_move(10), size_field)
            else:
                x, y = self.parse.parse(self.input_output.input_str(), size_field)
                #x, y = self.parse.parse(self.input_output.input_from_array(i),size_field)
                #i += 1
            #print(x, y)
            if x == 0 and y == 0:
                if num_of_players == 2:
                    self.input_output.output_exe()
                continue

            if self.state == 'seating':
                if self.whose_move_bool == 1:
                    if not self.player1.end_of_placement():
                        self.player1.put_ship(x, y)
                        print(self.player1.show_field_pattern().field_in_string())

                    elif self.player1.end_of_placement():
                        self.whose_move_bool *= -1
                        self.input_output.output_seating(2)
                        print(self.player2.show_field_pattern().field_in_string())

                elif self.whose_move_bool == -1 and not self.player2.end_of_placement():
                    self.player2.put_ship(x, y)
                    print(self.player2.show_field_pattern().field_in_string())

                else:
                    self.state = 'game'
                    self.input_output.output_finish_seating()
                    #print(self.player1.show_field_pattern().field_in_string())
                    #print(self.player1.show_field_pattern().field_in_string())

                    help_field = self.player1.field_pattern
                    self.player1.field_pattern = self.player2.field_pattern
                    self.player2.field_pattern = help_field
                    self.whose_move_bool = 1

                # вывод текущего заполнения
                #print(self.player1.show_field_pattern())

            if self.state == 'game':
                if self.player1.count_cell == 0:
                    self.input_output.output_win(1)
                    self.state = 'finish'

                elif self.player2.count_cell == 0:
                    self.input_output.output_win(2)
                    self.state = 'finish'
                else:
                    if self.whose_move_bool == 1:
                        self.whose_move_bool *= self.player1.do_step(x, y)
                        self.input_output.output_fields(self.player1.field_attack.field_in_string(),
                                                        self.player1.field_pattern.field_in_string(), 1)

                    else:
                        self.whose_move_bool *= self.player2.do_step(x, y)
                        self.input_output.output_fields(self.player2.field_attack.field_in_string(),
                                                        self.player2.field_pattern.field_in_string(), 2)


def main():
    game = Game()
    start = input('привет! давай играть! \n пиши\n 1 - игра с ботом \n 2 - игра с другом\n')

    while start != '1' or start != '2':
        if start == '1':
            game.run(1, 10)
        elif start == '2':
            game.run(2, 10)
        else:
            print('ой, ничего не понимаю, давай опробуем снова)')
            start = input('пиши\n 1 - игра с ботом \n 2 - игра с другом\n')


if __name__ == '__main__':
    main()
