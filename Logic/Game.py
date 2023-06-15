import sys
from PySide6.QtWidgets import (QApplication, QMainWindow)

from Handler.Output import Output
from Handler.Parse import Parse
from Handler.Save import Save

from Logic.Info import Info
from Player.BotPlayer import Bot

from gui.questions.QueSaveWindow import SaveWindow
from gui.questions.QueAvtoWindow import AvtoWindow
from gui.questions.QueFieldSizeWindow import FieldSizeWindow
from gui.questions.QueShipsWindow import ShipsWindow
from gui.questions.QueCountPlayersWindow import CountPlayersWindow
from gui.questions.QueDifficultlyWindow import DifficultlyWindow
from gui.questions.QueFillingWindow import FillingWindow
from gui.PlacementWindow import PlacementWindow
from gui.GameWindow import GameWindow
from gui.WinerWindow import WinnerWindow
from gui.StartWindow import StartWindow


class Game(Info):
    def __init__(self):
        super().__init__()
        self.output = Output()
        self.parse = Parse()
        self.save = Save()

    def start(self):
        """
        Запуск программы, открываем поток
        """
        app = QApplication(sys.argv)
        self.hello()
        sys.exit(app.exec())

    def hello(self):
        """
        Стартовое окно с кнопками (start, exit)
        """
        global start_window
        start_window = QMainWindow()
        self.window = StartWindow()
        self.save.is_saved()
        self.window.ui(start_window, self.save.is_saved_game)
        start_window.show()

        def close_():
            """
            выход из программы, активируется при нажатии кнопки (exit)
            """
            start_window.close()

        self.window.button_exit.clicked.connect(close_)
        self.window.button_start.clicked.connect(self.auto_window)
        if self.save.is_saved_game:
            self.window.button_save.clicked.connect(self.to_restore)

    def to_restore(self):
        """
        Восстановление из файла сохраненной игры
        """
        self.player1, self.player2, \
            self.is_move, self.ships, \
            self.field_size, self.count_players, \
            self.difficultly = self.save.to_restore()
        self.time = False
        self.game_window_()

    def auto_window(self):
        """
        Окно выбора автоматической настройки игры с кнопками (да, нет)
        по умолчанию (нет)
        """
        super().__init__()
        global auto_window
        auto_window = QMainWindow()
        self.window = AvtoWindow()
        self.window.ui(auto_window)
        start_window.close()
        auto_window.show()

        self.window.button_avto_yes.clicked.connect(self.click_button_auto_yes)
        self.window.button_avto_no.clicked.connect(self.field_size_window)

    def click_button_auto_yes(self):
        """
        автоматическая настройка игры
        активируется при нажатии кнопки (да)
        пропоскает все последующие настройки
        """
        auto_window.close()
        self.preparation()

    def field_size_window(self):
        """
        Окно выбора размера поля с кнопками (10, 15, 20)
        по умолчанию (10)
        """
        self.time = False
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
        """
        Изменение размера поля на 15
        """
        self.field_size = 15
        self.ships_window()

    def click_button_size_field_20(self):
        """
        Изменение размера поля на 20
        """
        self.field_size = 20
        self.ships_window()

    def ships_window(self):
        """
        Окно выбора кораблей с кнопками (прямые, угловые)
        о умолчанию (прямые)
        """
        global ships_window
        ships_window = QMainWindow()
        self.window = ShipsWindow()
        self.window.ui(ships_window)
        field_size_window.close()
        ships_window.show()

        self.window.button_ships_angular.clicked.connect(self.click_button_ships_angular)
        self.window.button_ships_straight.clicked.connect(self.count_players_window)

    def click_button_ships_angular(self):
        """
        Изменение кораблей на угловые
        """
        self.ships = 1
        self.count_players_window()

    def count_players_window(self):
        """
        Окно выбора количества игроков с кнопками (1, 2)
        1 - игра с ботом
        2 - игра с другом
        по умолчанию (1)
        """
        global count_players_window
        count_players_window = QMainWindow()
        self.window = CountPlayersWindow()
        self.window.ui(count_players_window)
        ships_window.close()
        count_players_window.show()

        self.window.button_game_with_friend.clicked.connect(self.click_button_game_with_friend)
        self.window.button_game_with_bot.clicked.connect(self.click_button_game_with_bot)

    def click_button_game_with_friend(self):
        """
        Изменение количества игроков на 2
        """
        self.count_players = 1
        count_players_window.close()
        self.filling_window()

    def click_button_game_with_bot(self):
        """
        Переход к уточняющему вопросу про сложность игры
        """
        count_players_window.close()
        self.difficultly_window()

    def difficultly_window(self):
        """
        Окно выбора сложности игры с кнопками (легкий, сложный)
        по умолчанию (легкий)
        активируется ТОЛЬКО, если выбрана игра с ботом
        """
        global difficultly_window
        difficultly_window = QMainWindow()
        self.window = DifficultlyWindow()
        self.window.ui(difficultly_window)
        count_players_window.close()
        difficultly_window.show()

        self.window.button_dfficultly_easy.clicked.connect(self.click_button_dfficultly_easy)
        self.window.button_dfficultly_hard.clicked.connect(self.click_button_dfficultly_hard)

    def click_button_dfficultly_hard(self):
        """
        Изменение сложности уровня игры на (сложный)
        """
        self.difficultly = 1
        difficultly_window.close()
        self.filling_window()

    def click_button_dfficultly_easy(self):
        """
        Переход к следующему вопросу
        """
        difficultly_window.close()
        self.filling_window()

    def filling_window(self):
        """
        Окно выбора расстановки кораблей с кнопками (бот, человек)
        по умолчанию (бот)
        """
        global filling_window
        filling_window = QMainWindow()
        self.window = FillingWindow()
        self.window.ui(filling_window)
        filling_window.show()

        self.window.button_settings_bot.clicked.connect(self.click_button_settings_bot)
        self.window.button_settings_hands.clicked.connect(self.click_button_settings_hands)

    def click_button_settings_hands(self):
        """
        Изменение способа расстановки кораблей на руной
        """
        self.filling = 1
        filling_window.close()
        self.preparation()

    def click_button_settings_bot(self):
        """
        Переход к уточняющему вопросу про игру на время
        """
        filling_window.close()
        self.preparation()

    def preparation(self):
        """
        Подготовка к игре
        создание игроков и заполнение всех необходимых полей
        """
        self.player1 = Bot(self.field_size, self.ships)
        self.player2 = Bot(self.field_size, self.ships)
        self.placement = 0

        if self.count_players == 0:  # бот+игрок
            self.placement_auto(self.player1)
            if self.filling == 0:  # игрок расставляет автоматически
                self.placement_auto(self.player2)
            else:  # игрок расставляет сам
                self.current_player = [self.player2, 2]
                self.placement_window_()

        if self.count_players == 1:  # игрок+игрок
            if self.filling == 0:  # игроки расставляют автоматически
                self.placement_auto(self.player1)
                self.placement_auto(self.player2)
            else:  # игроки расставляют сами
                self.current_player = [self.player1, 1]
                self.placement_window_()

    def placement_auto(self, player):
        """
        автоматическая генерация поля
        :param player: игрок у которого надо сгенерировать поле
        """
        while not player.end_of_placement():
            x, y = self.parse.parse(player.bot_generation_move(), self.field_size)
            if x == 0 and y == 0:
                continue
            player.put_ship(x, y)

        self.placement += 1
        if self.placement == 2:
            self.is_move = 1
            self.game_window_()

    def placement_window_(self):
        """
        Создание окна расстановки кораблей
        :param header_text: Текст заголовка (подсказка по работе)
        :param field: Поле расстановки
        """
        global placement_window
        placement_window = QMainWindow()
        self.window = PlacementWindow()
        self.window.ui(placement_window,
                       self.output.field(self.current_player[0].show_field_pattern().field,
                                         self.field_size,
                                         self.current_player[-1]), self.field_size, self.output.instructions())
        placement_window.show()

        self.window.button_enter_placement.clicked.connect(self.placement_player_move)

    def placement_player_move(self):
        """
        расстановка кораблей игроком
        """
        player = self.current_player[0]
        if not player.end_of_placement():
            x, y = self.parse.parse(self.window.text_enter_placement.text(), self.field_size)
            self.window.text_enter_placement.setText("")

            if x == 0 and y == 0:
                self.window.text_placement.setText(f'{self.output.instructions()}\n{self.output.error()}')
                return
            player.put_ship(x, y)
            self.window.text_placement.setText(f'{self.output.instructions()}')
            self.window.field_placement.setText(
                self.output.field(player.show_field_pattern().field, self.field_size,
                                  self.current_player[-1]))
        else:
            self.placement += 1

            if self.placement == 2:
                placement_window.close()
                self.is_move = 1
                self.game_window_()
            else:
                self.window.field_placement.setText(
                    self.output.field(self.player2.show_field_pattern().field, self.field_size, 2))
                self.current_player = [self.player2, 2]
                self.placement_player_move()

    def game_window_(self):
        """
        Создение окна игры с двумя полями игроков
        :param header_text: Текст заголовка (подсказка по работе)
        :param fields: Поля игры (поле игрока 1 и поле игрока 2)

        """
        help_field = self.player1.field_pattern
        self.player1.field_pattern = self.player2.field_pattern
        self.player2.field_pattern = help_field

        fields = self.output.fields(self.player1.show_field_attack().field,
                                    self.player2.show_field_attack().field, self.field_size, 1)
        global game_window
        game_window = QMainWindow()
        self.window = GameWindow()
        self.window.ui(game_window, self.output.instructions(), fields, self.field_size, self.time)
        if self.time:
            self.remaining_time = 5 * 60  # 5 минут
            self.window.timer.timeout.connect(self.update_timer)
        else:
            self.window.button_exit_game.clicked.connect(self.save_game_window)

        if self.count_players == 0:
            self.window.button_enter_game.clicked.connect(self.game_player_and_bot__moves)
        else:
            self.window.button_enter_game.clicked.connect(self.game_player_and_player__moves)

        game_window.show()

    def save_game_window(self):
        """
        Окно сохранения игры с кнопками (да, нет)
        """
        global save_window
        save_window = QMainWindow()
        self.window = SaveWindow()
        self.window.ui(save_window)
        save_window.show()

        def close_():
            """
            выход из программы, активируется при нажатии кнопки (exit)
            """
            game_window.close()
            save_window.close()
            self.hello()

        def save_():
            self.save.to_save(self.player1, self.player2, self.is_move, self.ships, self.field_size, self.count_players,
                              self.difficultly)
            close_()

        self.window.button_yes.clicked.connect(save_)
        self.window.button_no.clicked.connect(close_)

    def update_timer(self):
        """
        Обновление таймера и выход при завершении
        """
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.window.timer.stop()
            game_window.close()
            self.winner_window_()
        else:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.window.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def game_player_and_bot__moves(self):
        """
        Игра бота и человека
        """
        if self.player1.count_cell != 0 and self.player2.count_cell != 0:
            x, y = self.parse.parse(self.window.text_enter_game.text(), self.field_size)
            self.window.text_enter_game.setText("")

            if x == 0 and y == 0:
                self.window.text_game.setText(f'{self.output.instructions()}\n{self.output.error()}')
                return

            step = self.player2.do_step(x, y)
            if step == 0:
                self.window.text_game.setText(f'{self.output.instructions()}\n{self.output.error()}')

                return
            self.is_move *= step

            self.window.text_game.setText(f'{self.output.instructions()}')
            self.window.field_game.setText(self.output.fields(self.player1.show_field_attack().field,
                                                              self.player2.show_field_attack().field,
                                                              self.field_size, 2))
            while self.is_move == -1:
                if self.difficultly == 0:
                    x, y = self.parse.parse(self.player1.bot_generation_move(), self.field_size)
                else:
                    x, y = self.parse.parse(self.player1.bot_generation_rational_move(), self.field_size)

                step = self.player1.do_step(x, y)
                if step != 0:
                    self.is_move *= step
                    self.player1.last_move_x, self.player1.last_move_y = x, y

                self.window.field_game.setText(self.output.fields(self.player1.show_field_attack().field,
                                                                  self.player2.show_field_attack().field,
                                                                  self.field_size, 1))
        else:
            game_window.close()
            self.winner_window_()

    def game_player_and_player__moves(self):
        """
        игра двух людей
        """

        if self.player1.count_cell != 0 and self.player2.count_cell != 0:
            x, y = self.parse.parse(self.window.text_enter_game.text(), self.field_size)
            self.window.text_enter_game.setText("")
            if x == 0 and y == 0:
                self.window.text_game.setText(f'{self.output.instructions()}\n{self.output.error()}')
                return

            if self.is_move == 1:
                step = self.player1.do_step(x, y)
                if step == 0:
                    self.window.text_game.setText(f'{self.output.instructions()}\n{self.output.error()}')
                    return
                self.is_move *= step

            else:
                step = self.player2.do_step(x, y)
                if step == 0:
                    self.window.text_game.setText(f'{self.output.instructions()}\n{self.output.error()}')
                    return
                self.is_move *= step

            if self.is_move == 1:
                turn = 1
            else:
                turn = 2

            self.window.text_game.setText(f'{self.output.instructions()}')
            self.window.field_game.setText(self.output.fields(self.player1.show_field_attack().field,
                                                              self.player2.show_field_attack().field,
                                                              self.field_size, turn))
        else:
            game_window.close()
            self.winner_window_()

    def winner_window_(self):
        """
        Окно окно завершения игры с кнопкой (exit)
        :param text: текст для вывода результата победы
        """
        if self.player1.count_cell < self.player2.count_cell:
            text = self.output.win(2)

        elif self.player1.count_cell > self.player2.count_cell:
            text = self.output.win(1)

        else:
            text = self.output.draw()

        global winner_window_
        winner_window_ = QMainWindow()
        self.window = WinnerWindow()
        self.window.ui(winner_window_, text)

        def close_():
            """
            выход из программы, активируется при нажатии кнопки (exit)
            """
            winner_window_.close()

        def new_game():
            """
            переход к новой игре
            """
            close_()
            self.hello()

        winner_window_.show()
        self.window.button_exit.clicked.connect(close_)
        self.window.button_new_game.clicked.connect(new_game)
