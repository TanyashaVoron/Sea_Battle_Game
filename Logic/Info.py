from Handler.InputOutput import Input_Output


# класс, в котором хранится вся основная информация по игре, далее он него наследуется все

class Info:
    def __init__(self):
        self.field_size = 10  # размер поля 10/15/20
        self.ships = 0  # 1 - прямые | 2 - угловые
        self.count_players = 0  # 1 - с ботом | 2 - с другом
        self.difficultly = 0  # 1 - легкая сложность | 2 - сложная
        self.filling = 0  # 1 - расстановка ботом | 2 - расстановка руками
        self.time = False  # 0 - игра без времени | 1 - игра на время

        self.input_output = Input_Output()
        self.__set_info__()

    def __set_info__(self):
        if not self.__quick_start__():
            self.__field_size__()
            self.__ships__()
            self.__count_players__()
            self.__difficultly__()
            self.__filling__()
            self.__time__()

    def __quick_start__(self):
        ans = ['1', '2', 'yes', 'no', 'да', 'нет']
        self.input_output.questions_quick_start()
        quick_start = self.input_output.input()
        while quick_start not in ans:
            self.input_output.output_exe()
            quick_start = self.input_output.input()
        return ans.index(quick_start) % 2 == 0

    def __field_size__(self):
        size = [10, 15, 20, 1, 2, 3]
        self.input_output.questions_size_field()
        self.field_size = int(self.input_output.input())
        while self.field_size not in size:
            self.input_output.output_exe()
            self.field_size = int(self.input_output.input())
        self.field_size = size[size.index(self.field_size) % 3]

    def __ships__(self):
        ships = ['straight', 'angular', '1', '2', 'прямые', 'угловые']
        self.input_output.questions_ships()
        self.ships = self.input_output.input()
        while self.ships not in ships:
            self.input_output.output_exe()
            self.ships = self.input_output.input()
        self.ships = ships.index(self.ships) % 2

    def __count_players__(self):
        players = ['friend', 'bot', '1', '2', 'ты', 'друг']
        self.input_output.questions_count_players()
        self.count_players = self.input_output.input()
        while self.count_players not in players:
            self.input_output.output_exe()
            self.count_players = self.input_output.input()
        self.count_players = players.index(self.count_players) % 2

    def __difficultly__(self):
        difficultly = ['easy', 'hard', '1', '2', 'простой', 'сложный']
        self.input_output.questions_difficultly()
        self.difficultly = self.input_output.input()
        while self.difficultly not in difficultly:
            self.input_output.output_exe()
            self.difficultly = self.input_output.input()
        self.difficultly = difficultly.index(self.difficultly) % 2

    def __filling__(self):
        filling = ['machine', 'hands', '1', '2', 'автоматически', 'сам']
        self.input_output.questions_filling()
        self.filling = self.input_output.input()
        while self.filling not in filling:
            self.input_output.output_exe()
            self.filling = self.input_output.input()
        self.filling = filling.index(self.filling) % 2

    def __time__(self):
        time = ['1', '2', 'yes', 'no', 'да', 'нет']
        self.input_output.questions_time()
        self.time = self.input_output.input()
        while self.time not in time:
            self.input_output.output_exe()
            self.time = self.input_output.input()
        self.time = time.index(self.time) % 2
