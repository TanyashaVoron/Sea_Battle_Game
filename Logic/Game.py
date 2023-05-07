from Logic.Info import Info
from Player.BotPlayer import Bot
from Handler.Parse import Parse


class Game(Info):
    def __init__(self):
        super().__init__()

        self.parse = Parse()

        self.player1 = Bot(self.field_size, self.ships)
        self.function_seating_move_player1 = self.input_output.input_coordinates
        self.function_game_move_player1 = self.input_output.input_coordinates

        self.player2 = Bot(self.field_size, self.ships)
        self.function_seating_move_player2 = self.input_output.input_coordinates
        self.function_game_move_player2 = self.input_output.input_coordinates
        self.__setup_players__()

        self.state = 'start'
        self.whose_move_bool = 1

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
    def __move_request__(self):
        if self.whose_move_bool == 1:
            if self.state == 'seating':
                return self.parse.parse(self.function_seating_move_player1(), self.field_size)
            if self.state == 'Handler':
                return self.parse.parse(self.function_game_move_player1(), self.field_size)
        if self.whose_move_bool != 1:
            if self.state == 'seating':
                return self.parse.parse(self.function_seating_move_player2(), self.field_size)
            if self.state == 'Handler':
                return self.parse.parse(self.function_game_move_player2(), self.field_size)

    def __state_start__(self):
        self.state = 'seating'
        if self.filling != 0:
            self.input_output.output_seating(1)
            self.input_output.output_field(self.player1.show_field_pattern().field, self.field_size)

    def __state_seating__(self, x, y):
        if self.whose_move_bool == 1 and not self.player1.end_of_placement():
            if not self.player1.end_of_placement():
                self.player1.put_ship(x, y)
                if self.filling != 0:
                    self.input_output.output_field(self.player1.show_field_pattern().field, self.field_size)  #

            elif self.player1.end_of_placement():
                self.whose_move_bool *= -1
                if self.filling != 0 and self.count_players != 0:
                    self.input_output.output_seating(2)
                    self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size)  #

        elif self.whose_move_bool == -1 and not self.player2.end_of_placement():
            self.player2.put_ship(x, y)
            if self.filling != 0 and self.count_players != 0:
                self.input_output.output_field(self.player2.show_field_pattern().field, self.field_size)  #

        else:
            self.state = 'Handler'
            self.input_output.output_finish_seating()
            help_field = self.player1.field_pattern
            self.player1.field_pattern = self.player2.field_pattern
            self.player2.field_pattern = help_field
            self.whose_move_bool = -1
            self.input_output.output_fields(self.player1.show_field_pattern().field,
                                            self.player2.show_field_pattern().field, self.field_size)

    def __state_game__(self, x, y):
        if self.player1.count_cell == 0:
            self.input_output.output_win(2)
            self.state = 'finish'

        elif self.player2.count_cell == 0:
            self.input_output.output_win(1)
            self.state = 'finish'

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
            self.input_output.output_fields(self.player1.show_field_attack().field,
                                            self.player2.show_field_attack().field, self.field_size)

    def run(self):
        while self.state != 'finish':

            if self.state == 'start':
                self.__state_start__()

            x, y = self.__move_request__()

            if x == 0 and y == 0:
                if self.count_players == 1 or (self.count_players == 0 and self.whose_move_bool == 1):
                    self.input_output.output_exe()
                continue

            self.player2.set_last_move_xy(x, y)

            if self.state == 'seating':
                self.__state_seating__(x, y)

            if self.state == 'Handler':
                if self.whose_move_bool == 1:
                    self.input_output.output_str('player number 2 turn')
                else:
                    self.input_output.output_str('player number 1 turn')
                self.__state_game__(x, y)
