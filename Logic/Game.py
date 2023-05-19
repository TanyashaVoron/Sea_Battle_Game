import sys

from Handler.InputOutput import Input_Output
from Logic.Info import Info
from Player.BotPlayer import Bot
from Handler.Parse import Parse


class Game(Info):
    def __init__(self):
        super().__init__()
        self.input_output = Input_Output()
        self.parse = Parse()
        self.state = 'start'
        self.whose_move_bool = 1

    def preparation_(self):
        self.player1 = Bot(self.field_size, self.ships)
        self.player2 = Bot(self.field_size, self.ships)
        self.function_seating_move_player1 = "input"
        self.function_game_move_player1 = "input"
        self.function_seating_move_player2 = "input"
        self.function_game_move_player2 = "input"
        self.__setup_players__()



    # изменяем метод хода и при расстановке и игре в зависимости от введенных данных
    def __setup_players__(self):
        if self.count_players == 0:
            if self.filling == 0:
                self.function_seating_move_player1 = self.player1.bot_generation_move
            self.function_seating_move_player2 = self.player2.bot_generation_move
            self.function_game_move_player2 = self.player2.bot_generation_move
            if self.difficultly == 1:
                self.function_game_move_player2 = self.player2.bot_generation_rational_move
        if self.count_players != 0 and self.filling == 0:
            self.function_seating_move_player2 = self.player2.bot_generation_move
            self.function_seating_move_player1 = self.player1.bot_generation_move

    # запрос хода
    def __move_request__(self, coordinate='-1'):
        if self.whose_move_bool == 1:
            if self.state == 'seating':
                if self.function_seating_move_player1 == 'input':
                    return self.parse.parse(coordinate, self.field_size)
                else:
                    return self.parse.parse(self.function_seating_move_player1(), self.field_size)
            if self.state == 'Handler':
                if self.function_game_move_player1 == 'input':
                    return self.parse.parse(coordinate, self.field_size)
                else:
                    return self.parse.parse(self.function_game_move_player1(), self.field_size)
        if self.whose_move_bool != 1:
            if self.state == 'seating':
                if self.function_seating_move_player2 == 'input':
                    return self.parse.parse(coordinate, self.field_size)
                else:
                    return self.parse.parse(self.function_seating_move_player2(), self.field_size)
            if self.state == 'Handler':
                if self.function_game_move_player2 == 'input':
                    return self.parse.parse(coordinate, self.field_size)
                else:
                    return self.parse.parse(self.function_game_move_player2(), self.field_size)

    def __state_start__(self):
        self.state = 'seating'
        if self.filling != 0:
            return self.input_output.output_field(self.player1.show_field_pattern().field, self.field_size, 1)
        return '*'

    def __state_seating__(self, x, y):
        if self.whose_move_bool == 1 and not self.player1.end_of_placement():
            if not self.player1.end_of_placement():
                self.player1.put_ship(x, y)
                print(self.input_output.output_field(self.player1.show_field_pattern().field, self.field_size,
                                                          1))
                if self.filling != 0:
                    return self.input_output.output_field(self.player1.show_field_pattern().field, self.field_size,
                                                          1)  #

            elif self.player1.end_of_placement():
                self.whose_move_bool *= -1
                print(self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size,
                                                          2))
                if self.filling != 0 and self.count_players != 0:
                    return self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size,
                                                          2)  #

        elif self.whose_move_bool == -1 and not self.player2.end_of_placement():
            self.player2.put_ship(x, y)
            print(self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size, 2))
            if self.filling != 0 and self.count_players != 0:
                return self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size, 2)  #

        else:
            self.state = 'Handler'
            # self.input_output.output_finish_seating()
            help_field = self.player1.field_pattern
            self.player1.field_pattern = self.player2.field_pattern
            self.player2.field_pattern = help_field
            self.whose_move_bool = -1
            # self.input_output.output_fields(self.player1.show_field_pattern().field, self.player2.show_field_pattern().field, self.field_size)
        return '*'

    def __state_game__(self, x, y, turn):
        if self.player1.count_cell == 0:
            self.state = 'finish'
            return self.input_output.output_win(2)

        elif self.player2.count_cell == 0:
            self.state = 'finish'
            return self.input_output.output_win(1)
        else:
            if self.whose_move_bool == 1:
                step = self.player1.do_step(x, y)
                if step != 0:
                    self.whose_move_bool *= step
                # self.input_output.output_fields(self.player1.show_field_attack().field,self.player1.show_field_pattern().field, 1, self.field_size)

            else:
                step = self.player2.do_step(x, y)
                if step != 0:
                    self.whose_move_bool *= step
                # self.input_output.output_fields(self.player2.show_field_attack().field,self.player2.show_field_pattern().field, 2, self.field_size)
            return self.input_output.output_fields(self.player1.show_field_attack().field,
                                                   self.player2.show_field_attack().field, self.field_size, turn)
