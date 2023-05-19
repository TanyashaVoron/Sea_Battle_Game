from Logic.Game import Game
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow)

from gui.GameWindow import GameWindow
from gui.PlacementWindow import PlacementWindow
from gui.WinerWindow import WinnerWindow
from gui.questions.QueAvtoWindow import AvtoWindow
from gui.questions.QueDifficultlyWindow import DifficultlyWindow
from gui.questions.QueCountPlayersWindow import CountPlayersWindow
from gui.questions.QueFillingWindow import FillingWindow
from gui.questions.QueShipsWindow import ShipsWindow
from gui.questions.QueTimeWindow import TimeWindow
from gui.questions.StartWindow import StartWindow
from gui.questions.QueFieldSizeWindow import FieldSizeWindow


class LigicGUI(Game):
    def __init__(self):

        super().__init__()
        self.placement_window_is_open = False
        self.game_window_is_open = False
        self.current_text = ''
        self.coordinate_input = "введите координаты\n(без пробелов цифра, буква)\nнажмите кнопку ВВОД"
        self.bot_generation = 'бот генерирует поле, подожди немного'
        self.exe = 'ошибка ввода. попробуйте еще раз'

    def start(self):  # стартовое окно
        self.app = QApplication(sys.argv)
        global start_window
        start_window = QMainWindow()
        self.window = StartWindow()
        self.window.ui(start_window)
        start_window.show()

        def close_():
            start_window.close()

        self.window.button_exit.clicked.connect(close_)
        self.window.button_start.clicked.connect(self.auto_window)
        sys.exit(self.app.exec())

    def auto_window(self):
        global auto_window
        auto_window = QMainWindow()
        self.window = AvtoWindow()
        self.window.ui(auto_window)
        start_window.close()
        auto_window.show()

        self.window.button_avto_yes.clicked.connect(self.click_button_avto_no)
        self.window.button_avto_no.clicked.connect(self.field_size_window)

    def click_button_avto_no(self):
        auto_window.close()
        self.preparation()

    def field_size_window(self):  # окно выбора размера поля
        global field_size_window
        field_size_window = QMainWindow()
        self.window = FieldSizeWindow()
        self.window.ui(field_size_window)
        auto_window.close()
        field_size_window.show()

        self.window.button_size_field_15.clicked.connect(self.click_button_size_field_15)
        self.window.button_size_field_20.clicked.connect(self.click_button_size_field_20)
        self.window.button_size_field_10.clicked.connect(self.ships_window)

    def click_button_size_field_15(self):
        self.field_size = 15
        self.ships_window()

    def click_button_size_field_20(self):
        self.field_size = 20
        self.ships_window()

    def ships_window(self):
        global ships_window
        ships_window = QMainWindow()
        self.window = ShipsWindow()
        self.window.ui(ships_window)
        field_size_window.close()
        ships_window.show()
        self.window.button_ships_angular.clicked.connect(self.click_button_ships_angular)
        self.window.button_ships_straight.clicked.connect(self.count_players_window)

    def click_button_ships_angular(self):
        self.ships = 1
        self.count_players_window()

    def count_players_window(self):
        global count_players_window
        count_players_window = QMainWindow()
        self.window = CountPlayersWindow()
        self.window.ui(count_players_window)
        ships_window.close()
        count_players_window.show()
        self.window.button_game_with_friend.clicked.connect(self.click_button_game_with_friend)
        self.window.button_game_with_bot.clicked.connect(self.click_button_game_with_bot)

    def click_button_game_with_friend(self):
        self.count_players = 1
        count_players_window.close()
        self.difficultly_window()

    def click_button_game_with_bot(self):
        count_players_window.close()
        self.difficultly_window()

    def difficultly_window(self):
        global difficultly_window
        difficultly_window = QMainWindow()
        self.window = DifficultlyWindow()
        self.window.ui(difficultly_window)
        count_players_window.close()
        difficultly_window.show()
        self.window.button_dfficultly_easy.clicked.connect(self.click_button_dfficultly_easy)
        self.window.button_dfficultly_hard.clicked.connect(self.click_button_dfficultly_hard)

    def click_button_dfficultly_hard(self):
        self.difficultly = 1
        difficultly_window.close()
        self.filling_window()

    def click_button_dfficultly_easy(self):
        difficultly_window.close()
        self.filling_window()

    def filling_window(self):
        global filling_window
        filling_window = QMainWindow()
        self.window = FillingWindow()
        self.window.ui(filling_window)

        filling_window.show()
        self.window.button_settings_bot.clicked.connect(self.click_button_settings_bot)
        self.window.button_settings_hands.clicked.connect(self.click_button_settings_hands)

    def click_button_settings_hands(self):
        self.filling = 1
        filling_window.close()
        self.preparation()

    def click_button_settings_bot(self):
        filling_window.close()
        self.preparation()

    def time_window(self):
        global time_window
        time_window = QMainWindow()
        self.window = TimeWindow()
        self.window.ui(time_window)

        time_window.show()
        self.window.button_time_yes.clicked.connect(self.click_button_time_yes)
        self.window.button_time_no.clicked.connect(self.click_button_time_no)

    def click_button_time_yes(self):
        self.time = 1
        # time_window.close()
        self.preparation()

    def click_button_time_no(self):
        # time_window.close()
        self.preparation()

    def preparation(self):
        self.preparation_()
        self.run()

    # pass
    # расстановка,
    # дописать в начало вопрос про стандартные настройки.
    # игра. в игре поле ввода и поле вывода. кнопка сделать ход
    # зименить размер авто поля подогнать под обычное поле

    # сделать логику отдельно. заполнение отдельно. использование отдельно
    #
    def placement_window_(self, header_text, text):
        self.ap = QApplication(sys.argv)
        global placement_window
        placement_window = QMainWindow()
        self.window = PlacementWindow()
        self.window.ui(placement_window, header_text, text)

        placement_window.show()
        self.window.button_enter.clicked.connect(self.run)

    def game_window_(self, header_text, text):
        #self.a = QApplication(sys.argv)
        global game_window
        game_window = QMainWindow()
        self.window = GameWindow()
        self.window.ui(game_window, header_text, text)

        game_window.show()
        self.window.button_enter.clicked.connect(self.run)

    def winner_window(self, text):
        global winner_window
        winner_window = QMainWindow()
        self.window = WinnerWindow()
        self.window.ui(winner_window, text)

        def close_():
            winner_window.close()

        winner_window.show()
        self.window.button_exit.clicked.connect(close_)

    def run(self):
        while self.state != 'finish':

            if self.state == 'start':
                self.current_text = self.__state_start__()
                if self.current_text != '*':
                    self.placement_window_is_open = True
                    self.placement_window_(self.current_text, self.coordinate_input)

            self.x_y = ''
            if self.placement_window_is_open or self.game_window_is_open:
                self.x_y = self.window.tex_enter.text()

                if self.game_window_is_open:
                    game_window.close()
                    self.game_window_is_open = False
                else:
                    placement_window.close()
                    self.placement_window_is_open = False

            x, y = self.__move_request__(self.x_y)
            print(x, y)
            if x == 0 and y == 0:
                if self.count_players == 1 or (self.count_players == 0 and self.whose_move_bool == 1):
                    if self.state == 'seating':
                        self.placement_window_is_open = True
                    else:
                        self.game_window_is_open = True
                    print(self.current_text)
                    self.placement_window_(self.current_text, self.coordinate_input + '\n' + self.exe)
                continue

            self.player2.set_last_move_xy(x, y)

            if self.state == 'seating':
                self.current_text = self.__state_seating__(x, y)
                print(self.current_text)
                if self.current_text != '*':
                    self.placement_window_is_open = True
                    self.placement_window_(self.current_text, self.coordinate_input)

            if self.state == 'Handler':
                if self.whose_move_bool == 1:
                    turn = 1
                else:
                    turn = 2
                self.current_text = self.__state_game__(x, y, turn)

                if self.current_text[:4] != 'поб':
                    if self.whose_move_bool != 1 or self.count_players != 0:
                        self.game_window_is_open = True
                        self.game_window_(self.current_text, self.coordinate_input)
                    sys.exit(self.ap.exec())

                else:
                    self.winner_window(self.current_text)
                    # sys.exit(self.ap.exec())
                    # sys.exit(self.a.exec())
